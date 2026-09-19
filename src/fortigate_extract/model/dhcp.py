from typing import Any

from pydantic import BaseModel, Field


class FGDHCPIPRange(BaseModel):
    id: int

    start_ip: str | None = None
    end_ip: str | None = None
    lease_time: int | None = None

    raw_extra: dict[str, Any] = Field(default_factory=dict)
    explicit_fields: set[str] = Field(default_factory=set)


class FGDHCPExcludeRange(BaseModel):
    id: int

    start_ip: str | None = None
    end_ip: str | None = None

    raw_extra: dict[str, Any] = Field(default_factory=dict)
    explicit_fields: set[str] = Field(default_factory=set)


class FGDHCPReservedAddress(BaseModel):
    id: int

    ip: str | None = None
    mac: str | None = None
    description: str | None = None

    action: str | None = None
    type: str | None = None

    raw_extra: dict[str, Any] = Field(default_factory=dict)
    explicit_fields: set[str] = Field(default_factory=set)


class FGDHCPServer(BaseModel):
    id: int
    vdom: str = "root"

    # Binding / state
    interface: str | None = None
    status: str | None = None
    server_type: str | None = None
    ip_mode: str | None = None

    # Core network settings
    default_gateway: str | None = None
    netmask: str | None = None
    lease_time: int | None = None

    # DNS
    dns_service: str | None = None
    dns_servers: list[str] = Field(default_factory=list)

    # Timezone
    timezone_option: str | None = None
    timezone: str | None = None

    # Relay
    relay_agent: str | None = None

    # Address pools / exclusions / reservations
    ip_ranges: list[FGDHCPIPRange] = Field(default_factory=list)
    exclude_ranges: list[FGDHCPExcludeRange] = Field(default_factory=list)
    reserved_addresses: list[FGDHCPReservedAddress] = Field(default_factory=list)

    # Preserve unsupported source fields
    raw_extra: dict[str, Any] = Field(default_factory=dict)
    explicit_fields: set[str] = Field(default_factory=set)