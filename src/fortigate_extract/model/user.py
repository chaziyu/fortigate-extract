from typing import Any

from pydantic import BaseModel, Field


class FGLocalUser(BaseModel):
    name: str
    vdom: str = "root"

    # Identity / state
    id: int | None = None
    status: str | None = None
    type: str | None = None

    # Credential metadata
    passwd_time: str | None = None
    passwd_policy: str | None = None

    # External authentication references
    ldap_server: str | None = None
    radius_server: str | None = None
    tacacs_server: str | None = None

    # Two-factor
    two_factor: str | None = None
    two_factor_authentication: str | None = None
    two_factor_notification: str | None = None

    fortitoken: str | None = None
    email_to: str | None = None
    sms_phone: str | None = None
    sms_server: str | None = None
    sms_custom_server: str | None = None

    # Optional constraints
    workstation: str | None = None
    username_sensitivity: str | None = None

    # Secret presence only — never store secret values here
    password_configured: bool = False
    ppk_secret_configured: bool = False

    raw_extra: dict[str, Any] = Field(default_factory=dict)
    explicit_fields: set[str] = Field(default_factory=set)

class FGUserGroupMatch(BaseModel):
    id: int

    server_name: str | None = None
    group_name: str | None = None

    raw_extra: dict[str, Any] = Field(default_factory=dict)
    explicit_fields: set[str] = Field(default_factory=set)


class FGUserGroup(BaseModel):
    name: str
    vdom: str = "root"

    id: int | None = None
    group_type: str | None = None

    members: list[str] = Field(default_factory=list)
    matches: list[FGUserGroupMatch] = Field(default_factory=list)

    # Optional authentication behavior
    authtimeout: int | None = None
    auth_concurrent_override: str | None = None
    auth_concurrent_value: int | None = None

    raw_extra: dict[str, Any] = Field(default_factory=dict)
    explicit_fields: set[str] = Field(default_factory=set)