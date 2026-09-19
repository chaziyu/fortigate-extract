from typing import Any

from pydantic import BaseModel, Field

class FGSSLVPNSettings(BaseModel):
    vdom: str = "root"

    status: str | None = None

    # TLS / authentication
    ssl_min_proto_ver: str | None = None
    ssl_max_proto_ver: str | None = None
    auth_timeout: int | None = None
    idle_timeout: int | None = None

    # DNS
    dns_server1: str | None = None
    dns_server2: str | None = None

    # Certificate
    servercert: str | None = None

    # Source restrictions
    source_interfaces: list[str] = Field(default_factory=list)
    source_addresses: list[str] = Field(default_factory=list)

    # Tunnel pools
    tunnel_ip_pools: list[str] = Field(default_factory=list)
    tunnel_ipv6_pools: list[str] = Field(default_factory=list)

    # Portal
    default_portal: str | None = None

    # Listener
    port: int | None = None

    raw_extra: dict[str, Any] = Field(default_factory=dict)
    explicit_fields: set[str] = Field(default_factory=set)

class FGSSLVPNPortal(BaseModel):
    name: str
    vdom: str = "root"

    # Tunnel access
    tunnel_mode: str | None = None
    ipv6_tunnel_mode: str | None = None

    # Address pools
    ip_pools: list[str] = Field(default_factory=list)
    ipv6_pools: list[str] = Field(default_factory=list)

    # Split tunneling
    split_tunneling: str | None = None
    split_tunneling_routing_addresses: list[str] = Field(
        default_factory=list
    )
    ipv6_split_tunneling: str | None = None
    ipv6_split_tunneling_routing_addresses: list[str] = Field(
        default_factory=list
    )

    # Session / client behavior
    limit_user_logins: str | None = None
    forticlient_download: str | None = None

    # Web/tunnel capability
    web_mode: str | None = None

    # Host checking
    host_check: str | None = None
    host_check_policy: list[str] = Field(default_factory=list)

    raw_extra: dict[str, Any] = Field(default_factory=dict)
    explicit_fields: set[str] = Field(default_factory=set)

class FGSSLVPNHostCheckItem(BaseModel):
    id: int

    action: str | None = None
    type: str | None = None
    target: str | None = None
    md5s: str | None = None
    version: str | None = None

    raw_extra: dict[str, Any] = Field(default_factory=dict)
    explicit_fields: set[str] = Field(default_factory=set)


class FGSSLVPNHostCheckSoftware(BaseModel):
    name: str
    vdom: str = "root"

    guid: str | None = None
    type: str | None = None
    os_type: str | None = None
    version: str | None = None

    check_items: list[FGSSLVPNHostCheckItem] = Field(
        default_factory=list
    )

    raw_extra: dict[str, Any] = Field(default_factory=dict)
    explicit_fields: set[str] = Field(default_factory=set)