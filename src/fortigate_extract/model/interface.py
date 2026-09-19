from typing import Any, Optional

from pydantic import BaseModel, Field


class FGInterface(BaseModel):

    # Identity / context
    name: str
    vdom: str = "root"

    alias: Optional[str] = None
    description: Optional[str] = None
    ip: Optional[str] = None

    # if got config secondaryip    
    secondary_ip_enabled: Optional[str] = None
    secondary_ips: list[FGInterfaceSecondaryIP] = Field(default_factory=list)

    type: Optional[str] = None
    role: Optional[str] = None
    mode: Optional[str] = None
    status: Optional[str] = None

    allowaccess: list[str] = Field(default_factory=list)

    # VLAN relationship
    vlanid: Optional[int] = None
    interface: Optional[str] = None

    # Aggregate / redundant topology
    members: list[str] = Field(default_factory=list)
    aggregate_parent: Optional[str] = None
    redundant_interface_parent: Optional[str] = None

    # Useful optional network context
    vrf: Optional[int] = None
    remote_ip: Optional[str] = None

    # Preserve explicit but currently unsupported settings.
    raw_extra: dict[str, Any] = Field(default_factory=dict)

    # Track what was actually present in source config.
    explicit_fields: set[str] = Field(default_factory=set)

# if got config secondaryip
class FGInterfaceSecondaryIP(BaseModel):
    id: int
    ip: Optional[str] = None
    allowaccess: list[str] = Field(default_factory=list)
    raw_extra: dict[str, Any] = Field(default_factory=dict)