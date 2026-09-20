from __future__ import annotations


SCHEMA_VERSION = 1


SCHEMA_SQL = """
CREATE TABLE report_metadata (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);


-- ================================================================
-- FortiGate source objects
-- ================================================================

CREATE TABLE source_objects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    domain TEXT NOT NULL,
    vdom TEXT NOT NULL,

    object_key TEXT NOT NULL,

    sort_order INTEGER NOT NULL,

    data_json TEXT NOT NULL
);

CREATE INDEX idx_source_objects_domain_vdom
ON source_objects (
    domain,
    vdom
);

CREATE INDEX idx_source_objects_domain_key
ON source_objects (
    domain,
    vdom,
    object_key
);


-- ================================================================
-- Interface topology
-- ================================================================

CREATE TABLE interface_topology (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    vdom TEXT NOT NULL,
    name TEXT NOT NULL,

    kind TEXT NOT NULL,
    parent TEXT,

    path_json TEXT NOT NULL,

    aggregate TEXT,

    physical_interfaces_json TEXT NOT NULL,
    issues_json TEXT NOT NULL
);

CREATE INDEX idx_interface_topology_name
ON interface_topology (
    vdom,
    name
);


-- ================================================================
-- VPN topology
-- ================================================================

CREATE TABLE vpn_topology (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    vdom TEXT NOT NULL,
    name TEXT NOT NULL,

    attached_interface TEXT,

    path_json TEXT NOT NULL,

    aggregate TEXT,

    physical_interfaces_json TEXT NOT NULL,
    issues_json TEXT NOT NULL
);

CREATE INDEX idx_vpn_topology_name
ON vpn_topology (
    vdom,
    name
);


-- ================================================================
-- Normalized services
-- ================================================================

CREATE TABLE normalized_services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    vdom TEXT NOT NULL,

    name TEXT NOT NULL,
    source_name TEXT,

    protocol TEXT NOT NULL,

    port TEXT,
    source_port TEXT,

    protocol_number INTEGER,

    icmp_type INTEGER,
    icmp_code INTEGER,

    comment TEXT
);

CREATE INDEX idx_normalized_services_name
ON normalized_services (
    vdom,
    name
);


CREATE TABLE normalized_service_groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    vdom TEXT NOT NULL,

    name TEXT NOT NULL,

    members_json TEXT NOT NULL,

    comment TEXT,

    generated INTEGER NOT NULL
);

CREATE INDEX idx_normalized_service_groups_name
ON normalized_service_groups (
    vdom,
    name
);


-- ================================================================
-- NAT
-- ================================================================

CREATE TABLE nat_rules (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    vdom TEXT NOT NULL,

    policy_id INTEGER,
    policy_name TEXT,

    translation_type TEXT NOT NULL,

    pool_names_json TEXT NOT NULL,
    translated_addresses_json TEXT NOT NULL,
    egress_interfaces_json TEXT NOT NULL,

    issues_json TEXT NOT NULL
);

CREATE INDEX idx_nat_policy
ON nat_rules (
    vdom,
    policy_id
);


-- ================================================================
-- Policy-name normalization
-- ================================================================

CREATE TABLE policy_names (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    vdom TEXT NOT NULL,

    policy_id INTEGER,

    source_name TEXT,
    normalized_name TEXT,

    truncated INTEGER NOT NULL,
    collision INTEGER NOT NULL
);

CREATE INDEX idx_policy_names_policy
ON policy_names (
    vdom,
    policy_id
);


-- ================================================================
-- VPN Phase 2 normalized selectors
-- ================================================================

CREATE TABLE vpn_phase2_normalized (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    vdom TEXT NOT NULL,

    name TEXT NOT NULL,
    phase1name TEXT,

    proposal_json TEXT NOT NULL,

    pfs TEXT,

    dhgrp_json TEXT NOT NULL,

    keylifeseconds INTEGER,
    keylifekbs INTEGER,

    source_range TEXT,
    destination_range TEXT
);

CREATE INDEX idx_vpn_phase2_name
ON vpn_phase2_normalized (
    vdom,
    name
);


-- ================================================================
-- Validation
-- ================================================================

CREATE TABLE validation_issues (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    severity TEXT NOT NULL,

    domain TEXT NOT NULL,
    vdom TEXT NOT NULL,

    object_name TEXT,
    field TEXT,

    message TEXT NOT NULL
);

CREATE INDEX idx_validation_severity
ON validation_issues (
    severity
);

CREATE INDEX idx_validation_domain
ON validation_issues (
    domain,
    vdom
);
"""