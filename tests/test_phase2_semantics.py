import unittest

from fortigate_extract.derived import build_derived_views
from fortigate_extract.model.interface import FGInterface
from fortigate_extract.model.policy import FGPolicy
from fortigate_extract.model.service import FGService
from fortigate_extract.model.source import FGConfig
from fortigate_extract.model.vip import FGVIP, FGVIPRealServer
from fortigate_extract.transform.nat import transform_nat
from fortigate_extract.transform.services import transform_services
from fortigate_extract.validation.models import ValidationSeverity
from fortigate_extract.validation.validator import validate_config


class Phase2SemanticTest(unittest.TestCase):
    def test_service_generated_state_is_explicit(self):
        result = transform_services(
            FGConfig(
                services=[
                    FGService(
                        name="multi",
                        tcp_portrange="80",
                        udp_portrange="53",
                    ),
                    FGService(
                        name="single",
                        protocol="TCP",
                        tcp_portrange="443",
                    ),
                ]
            )
        )

        self.assertEqual(
            [item.generated for item in result.services],
            [True, True, False],
        )

    def test_ambiguous_interface_nat_has_no_address(self):
        config = FGConfig(
            interfaces=[
                FGInterface(name="port1", ip="192.0.2.1/24"),
                FGInterface(name="port2", ip="192.0.2.2/24"),
            ],
            policies=[
                FGPolicy(
                    policy_id=1,
                    nat="enable",
                    dstintf=["port1", "port2"],
                )
            ],
        )

        result = transform_nat(config)[0]

        self.assertEqual(result.egress_interfaces, ("port1", "port2"))
        self.assertEqual(result.translated_addresses, ())
        self.assertTrue(result.issues)

    def test_broken_references_are_derived_once(self):
        derived = build_derived_views(
            FGConfig(
                policies=[FGPolicy(policy_id=2, srcaddr=["missing"])]
            )
        )

        self.assertEqual(len(derived.broken_references), 1)
        self.assertEqual(derived.broken_references[0].reference, "missing")

    def test_load_balancing_vip_requires_two_usable_backends(self):
        result = validate_config(
            FGConfig(
                vips=[
                    FGVIP(
                        name="vip",
                        type="load-balance",
                        realservers=[FGVIPRealServer(ip="192.0.2.10")],
                    )
                ]
            )
        )

        self.assertTrue(
            any(
                issue.domain == "vip"
                and issue.severity == ValidationSeverity.WARNING
                for issue in result.issues
            )
        )


if __name__ == "__main__":
    unittest.main()
