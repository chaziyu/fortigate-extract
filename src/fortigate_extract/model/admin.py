from typing import Any

from pydantic import BaseModel, Field


class FGAdministrator(BaseModel):
    name: str

    # Access control
    accprofile: str | None = None
    vdoms: list[str] = Field(default_factory=list)

    # Trusted hosts
    trusthosts: list[str] = Field(default_factory=list)
    ip6_trusthosts: list[str] = Field(default_factory=list)

    # Two-factor
    two_factor: str | None = None
    two_factor_authentication: str | None = None
    two_factor_notification: str | None = None

    fortitoken: str | None = None
    email_to: str | None = None
    sms_phone: str | None = None

    # Remote / certificate authentication
    remote_auth: str | None = None
    remote_group: str | None = None

    peer_auth: str | None = None
    peer_group: str | None = None

    # Optional login restriction
    schedule: str | None = None

    # Credential presence only
    password_configured: bool = False
    ssh_key_configured: bool = False

    # Metadata
    comments: str | None = None

    raw_extra: dict[str, Any] = Field(default_factory=dict)
    explicit_fields: set[str] = Field(default_factory=set)

class FGAdminProfile(BaseModel):
    name: str

    # Main permission groups
    authgrp: str | None = None
    ftviewgrp: str | None = None
    fwgrp: str | None = None
    loggrp: str | None = None
    netgrp: str | None = None
    secfabgrp: str | None = None
    sysgrp: str | None = None
    utmgrp: str | None = None
    vpngrp: str | None = None
    wanoptgrp: str | None = None
    wifi: str | None = None

    # Scope
    scope: str | None = None

    # CLI permissions
    cli_config: str | None = None
    cli_diagnose: str | None = None
    cli_exec: str | None = None
    cli_get: str | None = None
    cli_show: str | None = None

    # Timeout override
    admintimeout_override: str | None = None
    admintimeout: int | None = None

    comments: str | None = None

    raw_extra: dict[str, Any] = Field(default_factory=dict)
    explicit_fields: set[str] = Field(default_factory=set)