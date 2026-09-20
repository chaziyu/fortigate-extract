from __future__ import annotations

import io
import sys
from pathlib import Path

from flask import (
    Flask,
    jsonify,
    render_template,
    request,
    send_file,
)

from .config import ExtractionConfig
from .derived import build_derived_views
from .parser import parse_fortigate_config
from .extraction.extractor import extract_fortigate_config
from .validation.validator import validate_config
from .export.excel import export_excel


XLSX_MIMETYPE = (
    "application/"
    "vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)


class ConfigurationDecodeError(ValueError):
    """Raised when an uploaded configuration cannot be decoded."""


def _decode_configuration(
    raw: bytes,
    *,
    encoding: str = "utf-8",
) -> str:
    try:
        return raw.decode(encoding)

    except UnicodeDecodeError as exc:
        raise ConfigurationDecodeError(
            f"Configuration is not valid {encoding} "
            f"near byte offset {exc.start}."
        ) from exc


def _read_uploaded_config(
    config: ExtractionConfig,
) -> tuple[str, str]:
    """
    Read the uploaded FortiGate configuration.

    Returns:
        (filename, decoded_text)
    """

    uploaded = request.files.get("file")

    if uploaded is None or not uploaded.filename:
        raise ValueError(
            "A FortiGate configuration file is required."
        )

    raw = uploaded.read()

    if not raw:
        raise ValueError(
            "The uploaded configuration file is empty."
        )

    text = _decode_configuration(
        raw,
        encoding=config.encoding,
    )

    return uploaded.filename, text


def _config_summary(config) -> dict[str, int]:
    """
    Return source-model counts suitable for the web preview.
    """

    return {
        "interfaces": len(config.interfaces),
        "zones": len(config.zones),
        "addresses": len(config.addresses),
        "address_groups": len(config.address_groups),
        "services": len(config.services),
        "service_groups": len(config.service_groups),
        "policies": len(config.policies),
        "ip_pools": len(config.ip_pools),
        "vips": len(config.vips),
        "vip_groups": len(config.vip_groups),
        "static_routes": len(config.static_routes),
        "ipsec_phase1": len(config.ipsec_phase1),
        "ipsec_phase2": len(config.ipsec_phase2),
        "dhcp_servers": len(config.dhcp_servers),
        "local_users": len(config.local_users),
        "user_groups": len(config.user_groups),
        "administrators": len(config.administrators),
        "admin_profiles": len(config.admin_profiles),
        "ips_sensors": len(config.ips_sensors),
        "profile_groups": len(config.profile_groups),
    }


def _validation_summary(validation) -> dict:
    issues = list(
        getattr(validation, "issues", [])
    )

    severity_counts: dict[str, int] = {}

    for issue in issues:
        severity = str(
            getattr(issue, "severity", "unknown")
        )

        severity_counts[severity] = (
            severity_counts.get(severity, 0) + 1
        )

    return {
        "issue_count": len(issues),
        "severity_counts": severity_counts,
    }


def _run_extraction(
    text: str,
    config: ExtractionConfig,
):
    """
    Run the complete FortiGate extraction pipeline.

    Web and CLI must use the same pipeline.
    """

    tree = parse_fortigate_config(text)

    extracted = extract_fortigate_config(
        tree,
        config=config,
    )

    derived = build_derived_views(
        extracted.config
    )

    validation = validate_config(
        extracted.config,
        derived=derived,
    )

    return tree, extracted, derived, validation


def create_app(
    test_config: dict | None = None,
) -> Flask:
    """
    Create the FortiGate extraction web application.
    """

    if (
        getattr(sys, "frozen", False)
        and hasattr(sys, "_MEIPASS")
    ):
        base_dir = Path(sys._MEIPASS)

    else:
        base_dir = Path(__file__).resolve().parent

    app = Flask(
        __name__,
        static_folder=str(base_dir / "static"),
        template_folder=str(base_dir / "templates"),
    )

    app.config.update(
        TEMPLATES_AUTO_RELOAD=True,
        SEND_FILE_MAX_AGE_DEFAULT=0,
        MAX_CONTENT_LENGTH=32 * 1024 * 1024,
    )

    app.jinja_env.auto_reload = True

    if test_config:
        app.config.update(test_config)

    # ------------------------------------------------------------------
    # UI
    # ------------------------------------------------------------------

    @app.get("/")
    def index():
        return render_template("index.html")

    @app.get("/favicon.ico")
    def favicon():
        icon = Path(app.static_folder) / "app_icon.ico"

        if not icon.exists():
            return "", 404

        return send_file(
            icon,
            mimetype="image/vnd.microsoft.icon",
        )

    # ------------------------------------------------------------------
    # Health
    # ------------------------------------------------------------------

    @app.get("/api/health")
    def health():
        return jsonify(
            {
                "success": True,
                "service": "fortigate-extract",
            }
        )

    # ------------------------------------------------------------------
    # Preview
    # ------------------------------------------------------------------

    @app.post("/api/preview")
    def preview():
        """
        Parse and extract a FortiGate configuration without exporting Excel.
        """

        try:
            extraction_config = ExtractionConfig()

            filename, text = _read_uploaded_config(
                extraction_config
            )

            tree, extracted, derived, validation = _run_extraction(
                text,
                extraction_config,
            )

            return jsonify(
                {
                    "success": True,
                    "filename": filename,
                    "top_level_sections": len(tree.configs),
                    "objects": _config_summary(
                        extracted.config
                    ),
                    "validation": _validation_summary(
                        validation
                    ),
                }
            )

        except ConfigurationDecodeError as exc:
            return (
                jsonify(
                    {
                        "success": False,
                        "stage": "decode",
                        "error": str(exc),
                    }
                ),
                400,
            )

        except ValueError as exc:
            return (
                jsonify(
                    {
                        "success": False,
                        "error": str(exc),
                    }
                ),
                400,
            )

        except Exception as exc:
            app.logger.exception(
                "FortiGate preview failed"
            )

            return (
                jsonify(
                    {
                        "success": False,
                        "error": str(exc),
                    }
                ),
                500,
            )

    # ------------------------------------------------------------------
    # Excel extraction
    # ------------------------------------------------------------------

    @app.post("/api/extract/excel")
    def extract_excel():
        """
        Parse a FortiGate configuration and return the Excel report.
        """

        try:
            extraction_config = ExtractionConfig()

            filename, text = _read_uploaded_config(
                extraction_config
            )

            _, extracted, derived, validation = _run_extraction(
                text,
                extraction_config,
            )

            workbook = io.BytesIO()

            export_excel(
                extracted=extracted,
                derived=derived,
                validation=validation,
                output=workbook,
                config=extraction_config,
                source_name=filename,
            )

            workbook.seek(0)

            source_name = Path(filename).stem

            return send_file(
                workbook,
                mimetype=XLSX_MIMETYPE,
                as_attachment=True,
                download_name=(
                    f"{source_name}_fortigate_inventory.xlsx"
                ),
            )

        except ConfigurationDecodeError as exc:
            return (
                jsonify(
                    {
                        "success": False,
                        "stage": "decode",
                        "error": str(exc),
                    }
                ),
                400,
            )

        except ValueError as exc:
            return (
                jsonify(
                    {
                        "success": False,
                        "error": str(exc),
                    }
                ),
                400,
            )

        except Exception as exc:
            app.logger.exception(
                "FortiGate Excel extraction failed"
            )

            return (
                jsonify(
                    {
                        "success": False,
                        "error": str(exc),
                    }
                ),
                500,
            )

    return app


class DesktopAPI:
    """
    Small pywebview bridge.

    Keep this only if the desktop application is still required.
    """

    def __init__(self, window=None):
        self._window = window

    def set_window(self, window) -> None:
        self._window = window

    def save_file_dialog(
        self,
        filename: str,
        base64_data: str,
    ) -> dict:
        import base64

        try:
            import webview

            raw = base64.b64decode(base64_data)

            default_dir = Path.home() / "Downloads"

            if not default_dir.exists():
                default_dir = Path.home() / "Desktop"

            if self._window is None:
                return {
                    "success": False,
                    "error": "Desktop window is unavailable.",
                }

            dialog_type = getattr(
                webview,
                "FileDialog",
                None,
            )

            save_type = (
                webview.FileDialog.SAVE
                if dialog_type
                and hasattr(dialog_type, "SAVE")
                else getattr(
                    webview,
                    "SAVE_DIALOG",
                    30,
                )
            )

            result = self._window.create_file_dialog(
                dialog_type=save_type,
                directory=str(default_dir),
                save_filename=filename,
                file_types=(
                    "Excel Workbook (*.xlsx)",
                    "All files (*.*)",
                ),
            )

            if not result:
                return {
                    "success": False,
                    "cancelled": True,
                }

            path = (
                result[0]
                if isinstance(result, (list, tuple))
                else result
            )

            Path(path).write_bytes(raw)

            return {
                "success": True,
                "path": str(path),
            }

        except Exception as exc:
            return {
                "success": False,
                "error": str(exc),
            }


def run_desktop(
    port: int = 5000,
) -> None:
    """
    Launch the extraction UI as a desktop application.
    """

    app = create_app()

    try:
        import webview

        api = DesktopAPI()

        window = webview.create_window(
            title="FortiGate Configuration Extractor",
            url=app,
            width=1360,
            height=880,
            min_size=(960, 640),
            text_select=True,
            js_api=api,
        )

        api.set_window(window)

        webview.start(
            gui="edgechromium",
        )

    except ImportError:
        import webbrowser

        url = f"http://127.0.0.1:{port}"

        print(
            "pywebview is not installed. "
            f"Opening browser at {url}"
        )

        webbrowser.open(url)

        app.run(
            host="127.0.0.1",
            port=port,
            debug=False,
        )