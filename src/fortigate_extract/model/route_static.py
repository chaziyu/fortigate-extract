from typing import Any

from pydantic import BaseModel, Field


class FGStaticRoute(BaseModel):
    # Identity / context
    seq_num: int
    vdom: str = "root"

    # Destination
    dst: str | None = None
    dstaddr: str | None = None

    # Forwarding path
    device: str | None = None
    gateway: str | None = None
    dynamic_gateway: str | None = None

    # Route preference
    distance: int | None = None
    priority: int | None = None

    # Routing context
    vrf: int | None = None
    sdwan_zone: list[str] = Field(default_factory=list)

    # Optional source-specific routing
    src: str | None = None
    preferred_source: str | None = None

    # State / metadata
    status: str | None = None
    comment: str | None = None

    # Preserve explicit source fields outside current scope
    raw_extra: dict[str, Any] = Field(default_factory=dict)
    explicit_fields: set[str] = Field(default_factory=set)