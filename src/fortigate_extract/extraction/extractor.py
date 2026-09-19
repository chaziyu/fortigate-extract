from __future__ import annotations

from config import ExtractionConfig
from model.config import FGConfig
from nodes import FortiGateConfigTree

from .addresses import extract_addresses
from .interfaces import extract_interfaces
from .ip_pools import extract_ip_pools
from .result import ExtractionResult
from .schedules import extract_schedules
from .services import extract_services
from .vips import extract_vips


def extract_fortigate_config(
    tree: FortiGateConfigTree,
    *,
    config: ExtractionConfig,
) -> ExtractionResult:
    source = FGConfig()

    extract_interfaces(tree, source)

    extract_addresses(tree, source)
    extract_services(tree, source)
    extract_schedules(tree, source)

    extract_ip_pools(tree, source)
    extract_vips(tree, source)

    # Add the remaining domain extractors as they are migrated:
    #
    # extract_zones(tree, source)
    # extract_policies(tree, source)
    # extract_routes(tree, source)
    # extract_vpn(tree, source)
    # extract_dhcp(tree, source)
    # extract_sdwan(tree, source)
    # extract_ssl_vpn(tree, source)
    # extract_users(tree, source)
    # extract_admin(tree, source)
    # extract_ips(tree, source)
    # extract_profile_groups(tree, source)

    return ExtractionResult(
        config=source,
    )