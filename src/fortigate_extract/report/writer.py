from __future__ import annotations

import json
import os
import sqlite3
from dataclasses import asdict, is_dataclass
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any

from pydantic import BaseModel

from ..derived import DerivedViews
from ..model.source import FGConfig
from ..validation.models import ValidationResult

from .schema import (
    SCHEMA_SQL,
    SCHEMA_VERSION,
)


_SOURCE_COLLECTIONS: tuple[
    tuple[str, str],
    ...
] = (
    ("interface", "interfaces"),
    ("zone", "zones"),

    ("address", "addresses"),
    ("address_group", "address_groups"),
    ("wildcard_fqdn", "wildcard_fqdns"),

    ("service_category", "service_categories"),
    ("service", "services"),
    ("service_group", "service_groups"),

    ("ip_pool", "ip_pools"),

    ("vip", "vips"),
    ("vip_group", "vip_groups"),

    ("policy", "policies"),

    ("static_route", "static_routes"),

    ("ipsec_phase1", "ipsec_phase1"),
    ("ipsec_phase2", "ipsec_phase2"),

    ("dhcp_server", "dhcp_servers"),

    ("sdwan", "sdwans"),

    ("ips_sensor", "ips_sensors"),
    ("profile_group", "profile_groups"),

    ("ssl_vpn_settings", "ssl_vpn_settings"),
    ("ssl_vpn_portal", "ssl_vpn_portals"),

    # SSL-VPN host-check software intentionally excluded.

    ("local_user", "local_users"),
    ("user_group", "user_groups"),

    ("administrator", "administrators"),
    ("admin_profile", "admin_profiles"),

    ("external_resource", "external_resources"),
)


def write_report_database(
    output_path: Path,
    *,
    config: FGConfig,
    derived: DerivedViews,
    validation: ValidationResult,
    source_name: str | None = None,
) -> None:
    """
    Persist a completed FortiGate analysis report to SQLite.

    The database is built in a temporary file and atomically moved into
    place only after generation completes successfully.

    SQLite is a report/persistence layer only. It is not used by parsing,
    extraction, relationship resolution, transformation, or validation.
    """

    output_path = Path(output_path)

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    temporary_path = output_path.with_name(
        f".{output_path.name}.tmp"
    )

    if temporary_path.exists():
        temporary_path.unlink()

    connection: sqlite3.Connection | None = None

    try:
        connection = sqlite3.connect(
            temporary_path
        )

        _configure_writer_connection(
            connection
        )

        connection.executescript(
            SCHEMA_SQL
        )

        connection.execute(
            f"PRAGMA user_version = {SCHEMA_VERSION}"
        )

        with connection:
            _write_metadata(
                connection,
                source_name=source_name,
            )

            _write_source_objects(
                connection,
                config,
            )

            _write_interface_topology(
                connection,
                derived,
            )

            _write_vpn_topology(
                connection,
                derived,
            )

            _write_services(
                connection,
                derived,
            )

            _write_nat(
                connection,
                derived,
            )

            _write_policy_names(
                connection,
                derived,
            )

            _write_vpn_phase2(
                connection,
                derived,
            )

            _write_validation(
                connection,
                validation,
            )

        connection.execute(
            "PRAGMA optimize"
        )

        connection.close()
        connection = None

        os.replace(
            temporary_path,
            output_path,
        )

    except Exception:
        if connection is not None:
            connection.close()

        if temporary_path.exists():
            temporary_path.unlink()

        raise


def _configure_writer_connection(
    connection: sqlite3.Connection,
) -> None:
    """
    Optimize creation of a derived/rebuildable report database.

    The final report is protected by atomic file replacement, so durability
    settings during temporary database construction can favor throughput.
    """

    connection.execute(
        "PRAGMA journal_mode = OFF"
    )

    connection.execute(
        "PRAGMA synchronous = OFF"
    )

    connection.execute(
        "PRAGMA temp_store = MEMORY"
    )

    connection.execute(
        "PRAGMA foreign_keys = ON"
    )


def _write_metadata(
    connection: sqlite3.Connection,
    *,
    source_name: str | None,
) -> None:
    generated_at = (
        datetime.now(timezone.utc)
        .isoformat()
    )

    rows = (
        (
            "schema_version",
            str(SCHEMA_VERSION),
        ),
        (
            "format",
            "fortigate-report",
        ),
        (
            "generated_at_utc",
            generated_at,
        ),
        (
            "source_name",
            source_name or "",
        ),
    )

    connection.executemany(
        """
        INSERT INTO report_metadata (
            key,
            value
        )
        VALUES (?, ?)
        """,
        rows,
    )


def _write_source_objects(
    connection: sqlite3.Connection,
    config: FGConfig,
) -> None:
    rows: list[
        tuple[
            str,
            str,
            str,
            int,
            str,
        ]
    ] = []

    for domain, attribute in _SOURCE_COLLECTIONS:
        objects = getattr(
            config,
            attribute,
            (),
        )

        for index, obj in enumerate(
            objects
        ):
            rows.append(
                (
                    domain,
                    _object_vdom(
                        obj,
                    ),
                    _object_key(
                        domain,
                        obj,
                        index=index,
                    ),
                    index,
                    _json_dump(
                        obj
                    ),
                )
            )

    connection.executemany(
        """
        INSERT INTO source_objects (
            domain,
            vdom,
            object_key,
            sort_order,
            data_json
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        rows,
    )


def _write_interface_topology(
    connection: sqlite3.Connection,
    derived: DerivedViews,
) -> None:
    rows = (
        (
            item.vdom,
            item.name,
            item.kind,
            item.parent,
            _json_dump(
                item.path
            ),
            item.aggregate,
            _json_dump(
                item.physical_interfaces
            ),
            _json_dump(
                item.issues
            ),
        )
        for item
        in derived.topology.interfaces
    )

    connection.executemany(
        """
        INSERT INTO interface_topology (
            vdom,
            name,
            kind,
            parent,
            path_json,
            aggregate,
            physical_interfaces_json,
            issues_json
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        rows,
    )


def _write_vpn_topology(
    connection: sqlite3.Connection,
    derived: DerivedViews,
) -> None:
    rows = (
        (
            item.vdom,
            item.name,
            item.attached_interface,
            _json_dump(
                item.path
            ),
            item.aggregate,
            _json_dump(
                item.physical_interfaces
            ),
            _json_dump(
                item.issues
            ),
        )
        for item
        in derived.topology.vpns
    )

    connection.executemany(
        """
        INSERT INTO vpn_topology (
            vdom,
            name,
            attached_interface,
            path_json,
            aggregate,
            physical_interfaces_json,
            issues_json
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        rows,
    )


def _write_services(
    connection: sqlite3.Connection,
    derived: DerivedViews,
) -> None:
    service_rows = (
        (
            service.vdom,
            service.name,
            service.source_name,
            service.protocol,
            service.port,
            service.source_port,
            service.protocol_number,
            service.icmp_type,
            service.icmp_code,
            service.comment,
        )
        for service
        in derived.services.services
    )

    connection.executemany(
        """
        INSERT INTO normalized_services (
            vdom,
            name,
            source_name,
            protocol,
            port,
            source_port,
            protocol_number,
            icmp_type,
            icmp_code,
            comment
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        service_rows,
    )

    group_rows = (
        (
            group.vdom,
            group.name,
            _json_dump(
                group.members
            ),
            group.comment,
            int(
                group.generated
            ),
        )
        for group
        in derived.services.groups
    )

    connection.executemany(
        """
        INSERT INTO normalized_service_groups (
            vdom,
            name,
            members_json,
            comment,
            generated
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        group_rows,
    )


def _write_nat(
    connection: sqlite3.Connection,
    derived: DerivedViews,
) -> None:
    rows = (
        (
            nat.vdom,
            nat.policy_id,
            nat.policy_name,
            nat.translation_type,
            _json_dump(
                nat.pool_names
            ),
            _json_dump(
                nat.translated_addresses
            ),
            _json_dump(
                nat.egress_interfaces
            ),
            _json_dump(
                nat.issues
            ),
        )
        for nat
        in derived.nat
    )

    connection.executemany(
        """
        INSERT INTO nat_rules (
            vdom,
            policy_id,
            policy_name,
            translation_type,
            pool_names_json,
            translated_addresses_json,
            egress_interfaces_json,
            issues_json
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        rows,
    )


def _write_policy_names(
    connection: sqlite3.Connection,
    derived: DerivedViews,
) -> None:
    rows = (
        (
            item.vdom,
            item.policy_id,
            item.source_name,
            item.normalized_name,
            int(
                item.truncated
            ),
            int(
                item.collision
            ),
        )
        for item
        in derived.policy_names
    )

    connection.executemany(
        """
        INSERT INTO policy_names (
            vdom,
            policy_id,
            source_name,
            normalized_name,
            truncated,
            collision
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        rows,
    )


def _write_vpn_phase2(
    connection: sqlite3.Connection,
    derived: DerivedViews,
) -> None:
    rows = (
        (
            item.vdom,
            item.name,
            item.phase1name,
            _json_dump(
                item.proposal
            ),
            item.pfs,
            _json_dump(
                item.dhgrp
            ),
            item.keylifeseconds,
            item.keylifekbs,
            item.source_range,
            item.destination_range,
        )
        for item
        in derived.vpn.phase2
    )

    connection.executemany(
        """
        INSERT INTO vpn_phase2_normalized (
            vdom,
            name,
            phase1name,
            proposal_json,
            pfs,
            dhgrp_json,
            keylifeseconds,
            keylifekbs,
            source_range,
            destination_range
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        rows,
    )


def _write_validation(
    connection: sqlite3.Connection,
    validation: ValidationResult,
) -> None:
    rows = (
        (
            issue.severity.value,
            issue.domain,
            issue.vdom,
            issue.object_name,
            issue.field,
            issue.message,
        )
        for issue
        in validation.issues
    )

    connection.executemany(
        """
        INSERT INTO validation_issues (
            severity,
            domain,
            vdom,
            object_name,
            field,
            message
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        rows,
    )


def _object_vdom(
    obj: Any,
) -> str:
    value = getattr(
        obj,
        "vdom",
        None,
    )

    if value:
        return str(value)

    return "global"


def _object_key(
    domain: str,
    obj: Any,
    *,
    index: int,
) -> str:
    name = getattr(
        obj,
        "name",
        None,
    )

    if name not in {
        None,
        "",
    }:
        return str(name)

    for attribute in (
        "policy_id",
        "seq_num",
        "id",
    ):
        value = getattr(
            obj,
            attribute,
            None,
        )

        if value is not None:
            return str(value)

    if domain == "sdwan":
        return "sdwan"

    if domain == "ssl_vpn_settings":
        return "settings"

    return (
        f"{domain}-{index + 1}"
    )


def _json_dump(
    value: Any,
) -> str:
    return json.dumps(
        _json_ready(value),
        ensure_ascii=False,
        separators=(
            ",",
            ":",
        ),
        sort_keys=True,
    )


def _json_ready(
    value: Any,
) -> Any:
    """
    Convert report data into JSON-safe values.

    raw_extra and explicit_fields are deliberately not persisted.

    raw_extra may contain unsupported FortiGate source settings and therefore
    must not be treated as safe report data.
    """

    if isinstance(
        value,
        BaseModel,
    ):
        return _json_ready(
            value.model_dump(
                mode="python"
            )
        )

    if is_dataclass(value):
        return _json_ready(
            asdict(value)
        )

    if isinstance(
        value,
        Enum,
    ):
        return value.value

    if isinstance(
        value,
        dict,
    ):
        result: dict[str, Any] = {}

        for key, item in value.items():
            key = str(key)

            if key in {
                "raw_extra",
                "explicit_fields",
            }:
                continue

            result[key] = (
                _json_ready(item)
            )

        return result

    if isinstance(
        value,
        (
            list,
            tuple,
        ),
    ):
        return [
            _json_ready(item)
            for item in value
        ]

    if isinstance(
        value,
        set,
    ):
        return [
            _json_ready(item)
            for item in sorted(
                value,
                key=str,
            )
        ]

    if value is None:
        return None

    if isinstance(
        value,
        (
            str,
            int,
            float,
            bool,
        ),
    ):
        return value

    return str(value)