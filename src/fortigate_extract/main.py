from __future__ import annotations

import sys
from pathlib import Path

import click

from config import ExtractionConfig
from parser import parse_fortigate_config
from extraction.extractor import extract_fortigate_config
from validation.validator import validate_config
from export.excel import export_excel


@click.group()
def cli() -> None:
    """Extract FortiGate configuration into structured Excel reports."""


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
    help="Output Excel file (.xlsx).",
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
    """Extract a FortiGate configuration to Excel."""

    try:
        extraction_config = (
            ExtractionConfig.from_yaml(config_path)
            if config_path
            else ExtractionConfig()
        )

        # --------------------------------------------------------------
        # 1. Read source configuration
        # --------------------------------------------------------------

        click.echo(f"Reading: {input_path}")

        text = input_path.read_text(
            encoding=extraction_config.encoding,
        )

        # --------------------------------------------------------------
        # 2. Parse CLI syntax into structural tree
        # --------------------------------------------------------------

        click.echo("Parsing FortiGate configuration...")

        tree = parse_fortigate_config(text)

        click.echo(
            f"  Parsed {len(tree.configs)} top-level config sections."
        )

        if tree.source_version:
            version_text = tree.source_version

            if tree.source_build:
                version_text += f" build {tree.source_build}"

            click.echo(f"  FortiOS: {version_text}")

        # --------------------------------------------------------------
        # 3. Extract FortiGate source models
        # --------------------------------------------------------------

        click.echo("Extracting FortiGate objects...")

        extracted = extract_fortigate_config(
            tree,
            config=extraction_config,
        )

        # --------------------------------------------------------------
        # 4. Validate extracted configuration
        # --------------------------------------------------------------

        click.echo("Validating extracted objects...")

        validation = validate_config(
            extracted.config,
        )

        # --------------------------------------------------------------
        # 5. Print summary
        # --------------------------------------------------------------

        _print_summary(
            extracted,
            validation,
        )

        # --------------------------------------------------------------
        # 6. Export Excel
        # --------------------------------------------------------------

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        click.echo(f"Writing Excel report: {output_path}")

        export_excel(
            extracted=extracted,
            validation=validation,
            output_path=output_path,
            config=extraction_config,
        )

        click.echo("Extraction complete.")

    except Exception as exc:
        click.echo(
            f"Extraction failed: {exc}",
            err=True,
        )

        raise click.Abort() from exc


def _print_summary(
    extracted,
    validation,
) -> None:
    """Print a compact extraction summary."""

    config = extracted.config

    counts = {
        "Interfaces": len(config.interfaces),
        "Zones": len(config.zones),
        "Addresses": len(config.addresses),
        "Address Groups": len(config.address_groups),
        "Services": len(config.services),
        "Service Groups": len(config.service_groups),
        "Policies": len(config.policies),
        "IP Pools": len(config.ip_pools),
        "VIPs": len(config.vips),
        "VIP Groups": len(config.vip_groups),
        "Static Routes": len(config.static_routes),
        "IPsec Phase 1": len(config.ipsec_phase1),
        "IPsec Phase 2": len(config.ipsec_phase2),
        "DHCP Servers": len(config.dhcp_servers),
        "Users": len(config.local_users),
        "User Groups": len(config.user_groups),
        "Administrators": len(config.administrators),
        "Admin Profiles": len(config.admin_profiles),
        "IPS Sensors": len(config.ips_sensors),
        "Profile Groups": len(config.profile_groups),
    }

    click.echo("")
    click.echo("Extraction summary")

    for label, count in counts.items():
        if count:
            click.echo(f"  {label:<20} {count}")

    issues = getattr(validation, "issues", [])

    if issues:
        click.echo("")
        click.echo(
            f"Validation issues: {len(issues)}"
        )


if __name__ == "__main__":
    cli()