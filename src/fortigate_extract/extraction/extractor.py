from __future__ import annotations

from ..config import ExtractionConfig
from ..model.source import FGConfig
from ..nodes import FortiGateConfigTree

from .address import extract_addresses
from .interfaces import extract_interfaces
from .ip_pools import extract_ip_pools
from .ips import extract_ips
from .policies import extract_policies
from .profile_groups import extract_profile_groups
from .result import ExtractionResult
from .routing import extract_routes
from .sdwan import extract_sdwan
from .services import extract_services
from .vips import extract_vips
from .vpn import extract_vpn


def extract_fortigate_config(
    tree: FortiGateConfigTree,
    *,
    config: ExtractionConfig,
) -> ExtractionResult:
    """
    Extract explicit FortiGate source configuration into small
    FortiGate source models.

    No canonical normalization, reference resolution, FortiOS defaults,
    or target-vendor conversion occurs here.
    """

    source = FGConfig()

    # Network topology source objects.
    extract_interfaces(tree, source)
    extract_zones(tree, source)

    # Reusable firewall objects.
    extract_addresses(tree, source)
    extract_services(tree, source)

    # NAT source objects.
    extract_ip_pools(tree, source)
    extract_vips(tree, source)

    # Policy source objects.
    extract_policies(tree, source)

    # Routing / VPN / SD-WAN source objects.
    extract_routes(tree, source)
    extract_vpn(tree, source)
    extract_sdwan(tree, source)

    # DHCP Server
    extract_dhcp(tree, source)

    # Security-profile source objects.
    extract_ips(tree, source)
    extract_profile_groups(tree, source)

    # User
    extract_users(tree, source)

    # Admin
    extract_admin(tree, source)

    return ExtractionResult(
        config=source,
    )