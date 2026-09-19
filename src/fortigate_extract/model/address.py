from typing import Any, Optional

from pydantic import BaseModel, Field

# config firewall address
class FGAddressTaggingEntry(BaseModel):
    name: str
    category: Optional[str] = None
    tags: list[str] = Field(default_factory=list)


class FGAddress(BaseModel):
    name: str
    vdom: str = "root"

    # Source type
    type: Optional[str] = None

    # Type-specific source values
    subnet: Optional[str] = None
    start_ip: Optional[str] = None
    end_ip: Optional[str] = None
    fqdn: Optional[str] = None
    wildcard: Optional[str] = None
    wildcard_fqdn: Optional[str] = None

    # Excel-visible metadata
    associated_interface: Optional[str] = None
    allow_routing: Optional[str] = None
    comment: Optional[str] = None

    # FortiGate tags
    tagging: list[FGAddressTaggingEntry] = Field(default_factory=list)

    # Preserve unsupported/unused explicit source fields
    raw_extra: dict[str, Any] = Field(default_factory=dict)
    explicit_fields: set[str] = Field(default_factory=set)


# config firewall addrgrp
class FGAddressGroupTaggingEntry(BaseModel):
    name: str
    category: str | None = None
    tags: list[str] = Field(default_factory=list)


class FGAddressGroup(BaseModel):
    name: str
    vdom: str = "root"

    # Core group contents
    members: list[str] = Field(default_factory=list)

    # Address exclusion
    exclude: str | None = None
    exclude_members: list[str] = Field(default_factory=list)

    # Description
    comment: str | None = None

    # Group semantics that may matter
    type: str | None = None
    category: str | None = None
    allow_routing: str | None = None

    # Optional object tagging
    tagging: list[FGAddressGroupTaggingEntry] = Field(default_factory=list)

    # Preserve explicit unsupported fields
    raw_extra: dict[str, Any] = Field(default_factory=dict)
    explicit_fields: set[str] = Field(default_factory=set)