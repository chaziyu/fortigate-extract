from __future__ import annotations

from pathlib import Path

import click

from .config import ExtractionConfig
from .derived import (
    DerivedViews,
    build_derived_views,
)
from .extraction.extractor import (
    extract_fortigate_config,
)
from .model.source import FGConfig
from .parser import parse_fortigate_config
from .report import write_report_database
from .validation.models import ValidationResult
from .validation.validator import validate_config


@click.group()
def cli() -> None:
    """
    Extract and analyze FortiGate configuration.

    Results are persisted as a SQLite-backed FortiGate report.
    """


@cli.command()
@click.option(
    "--input",
    "-i",
    "input_path",
    required=True,
    type=click.Path(
        exists=True,
        dir_okay=False,
        path_type=Path,
    ),
    help="FortiGate configuration file.",
)
@click.option(
    "--output",
    "-o",
    "output_path",
    required=True,
    type=click.Path(
        dir_okay=False,
        path_type=Path,
    ),
    help=(
        "Output FortiGate report database "
        "(.fgreport or .db)."
    ),
)
@click.option(
    "--config",
    "-c",
    "config_path",
    type=click.Path(
        exists=True,
        dir_okay=False,
        path_type=Path,
    ),
    help="Optional YAML extraction configuration.",
)
def extract(
    input_path: Path,
    output_path: Path,
    config_path: Path | None,
) -> None:
    """
    Parse, extract, analyze, validate, and persist a FortiGate report.
    """

    try:
        extraction_config = _load_config(
            config_path
        )

        # --------------------------------------------------------------
        # 1. Read source
        # --------------------------------------------------------------

        click.echo(
            f"Reading: {input_path}"
        )

        source_text = input_path.read_text(
            encoding=extraction_config.encoding,
        )

        # --------------------------------------------------------------
        # 2. Parse FortiGate CLI structure
        # --------------------------------------------------------------

        click.echo(
            "Parsing FortiGate configuration..."
        )

        tree = parse_fortigate_config(
            source_text
        )

        click.echo(
            "  Parsed "
            f"{len(tree.configs)} "
            "top-level config sections."
        )

        if tree.unknown_commands:
            click.echo(
                "  Preserved "
                f"{len(tree.unknown_commands)} "
                "unknown root command(s)."
            )

        # --------------------------------------------------------------
        # 3. Extract explicit FortiGate source objects
        # --------------------------------------------------------------

        click.echo(
            "Extracting FortiGate objects..."
        )

        extracted = extract_fortigate_config(
            tree,
            config=extraction_config,
        )

        source_config = extracted.config

        # --------------------------------------------------------------
        # 4. Build derived relationships / migration views
        # --------------------------------------------------------------

        click.echo(
            "Resolving relationships and "
            "building derived views..."
        )

        derived = build_derived_views(
            source_config
        )

        # --------------------------------------------------------------
        # 5. Validate
        # --------------------------------------------------------------

        click.echo(
            "Validating extracted configuration..."
        )

        validation = validate_config(
            source_config,
            derived=derived,
        )

        # --------------------------------------------------------------
        # 6. Print summary
        # --------------------------------------------------------------

        _print_summary(
            source_config,
            derived,
            validation,
        )

        # --------------------------------------------------------------
        # 7. Write SQLite report
        # --------------------------------------------------------------

        click.echo("")
        click.echo(
            f"Writing report: {output_path}"
        )

        write_report_database(
            output_path,
            config=source_config,
            derived=derived,
            validation=validation,
            source_name=input_path.name,
        )

        click.echo(
            "Report generation complete."
        )

    except (
        OSError,
        UnicodeError,
        ValueError,
    ) as exc:
        raise click.ClickException(
            f"Report generation failed: {exc}"
        ) from exc

    except Exception as exc:
        raise click.ClickException(
            f"Report generation failed: {exc}"
        ) from exc


def _load_config(
    config_path: Path | None,
) -> ExtractionConfig:
    if config_path is None:
        return ExtractionConfig()

    return ExtractionConfig.from_yaml(
        config_path
    )


def _print_summary(
    config: FGConfig,
    derived: DerivedViews,
    validation: ValidationResult,
) -> None:
    click.echo("")
    click.echo("FortiGate analysis summary")
    click.echo("--------------------------")

    source_counts = (
        (
            "Interfaces",
            len(config.interfaces),
        ),
        (
            "Zones",
            len(config.zones),
        ),
        (
            "Addresses",
            len(config.addresses),
        ),
        (
            "Address Groups",
            len(config.address_groups),
        ),
        (
            "Wildcard FQDNs",
            len(config.wildcard_fqdns),
        ),
        (
            "Services",
            len(config.services),
        ),
        (
            "Service Groups",
            len(config.service_groups),
        ),
        (
            "Policies",
            len(config.policies),
        ),
        (
            "IP Pools",
            len(config.ip_pools),
        ),
        (
            "VIPs",
            len(config.vips),
        ),
        (
            "VIP Groups",
            len(config.vip_groups),
        ),
        (
            "Static Routes",
            len(config.static_routes),
        ),
        (
            "IPsec Phase 1",
            len(config.ipsec_phase1),
        ),
        (
            "IPsec Phase 2",
            len(config.ipsec_phase2),
        ),
        (
            "DHCP Servers",
            len(config.dhcp_servers),
        ),
        (
            "SD-WAN",
            len(config.sdwans),
        ),
        (
            "SSL VPN Settings",
            len(config.ssl_vpn_settings),
        ),
        (
            "SSL VPN Portals",
            len(config.ssl_vpn_portals),
        ),
        (
            "Local Users",
            len(config.local_users),
        ),
        (
            "User Groups",
            len(config.user_groups),
        ),
        (
            "Administrators",
            len(config.administrators),
        ),
        (
            "Admin Profiles",
            len(config.admin_profiles),
        ),
        (
            "IPS Sensors",
            len(config.ips_sensors),
        ),
        (
            "Security Profile Groups",
            len(config.profile_groups),
        ),
        (
            "External Resources",
            len(config.external_resources),
        ),
    )

    for label, count in source_counts:
        if count:
            click.echo(
                f"  {label:<28} {count}"
            )

    click.echo("")
    click.echo("Derived views")

    derived_counts = (
        (
            "Interface Topology",
            len(
                derived.topology.interfaces
            ),
        ),
        (
            "VPN Topology",
            len(
                derived.topology.vpns
            ),
        ),
        (
            "Normalized Services",
            len(
                derived.services.services
            ),
        ),
        (
            "Normalized Service Groups",
            len(
                derived.services.groups
            ),
        ),
        (
            "NAT Rules",
            len(
                derived.nat
            ),
        ),
        (
            "Normalized Policy Names",
            len(
                derived.policy_names
            ),
        ),
        (
            "Normalized VPN Phase 2",
            len(
                derived.vpn.phase2
            ),
        ),
    )

    for label, count in derived_counts:
        if count:
            click.echo(
                f"  {label:<28} {count}"
            )

    click.echo("")
    click.echo("Validation")

    click.echo(
        f"  {'Errors':<28} "
        f"{len(validation.errors)}"
    )

    click.echo(
        f"  {'Warnings':<28} "
        f"{len(validation.warnings)}"
    )


if __name__ == "__main__":
    cli()