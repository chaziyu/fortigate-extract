from typing import Any

from pydantic import BaseModel, Field


class FGPolicy(BaseModel):
    # Identity / context
    policy_id: int
    vdom: str = "root"
    name: str | None = None

    # Interfaces
    srcintf: list[str] = Field(default_factory=list)
    dstintf: list[str] = Field(default_factory=list)

    # Addresses
    srcaddr: list[str] = Field(default_factory=list)
    dstaddr: list[str] = Field(default_factory=list)

    srcaddr6: list[str] = Field(default_factory=list)
    dstaddr6: list[str] = Field(default_factory=list)

    srcaddr_negate: str | None = None
    dstaddr_negate: str | None = None
    srcaddr6_negate: str | None = None
    dstaddr6_negate: str | None = None

    # Service / schedule
    service: list[str] = Field(default_factory=list)
    service_negate: str | None = None
    schedule: str | None = None

    # Action
    action: str | None = None

    # NAT
    nat: str | None = None
    ippool: str | None = None
    poolname: list[str] = Field(default_factory=list)
    poolname6: list[str] = Field(default_factory=list)

    # Internet Service matching
    internet_service: str | None = None
    internet_service_name: list[str] = Field(default_factory=list)
    internet_service_group: list[str] = Field(default_factory=list)
    internet_service_custom: list[str] = Field(default_factory=list)

    internet_service_src: str | None = None
    internet_service_src_name: list[str] = Field(default_factory=list)
    internet_service_src_group: list[str] = Field(default_factory=list)
    internet_service_src_custom: list[str] = Field(default_factory=list)

    # Security inspection
    utm_status: str | None = None
    inspection_mode: str | None = None

    profile_type: str | None = None
    profile_group: str | None = None

    av_profile: str | None = None
    ips_sensor: str | None = None
    application_list: str | None = None
    webfilter_profile: str | None = None
    dnsfilter_profile: str | None = None
    ssl_ssh_profile: str | None = None

    # Policy state / reporting
    status: str | None = None
    logtraffic: str | None = None
    comments: str | None = None

    # Preserve explicitly configured fields outside current scope
    raw_extra: dict[str, Any] = Field(default_factory=dict)
    explicit_fields: set[str] = Field(default_factory=set)