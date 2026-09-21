from __future__ import annotations

import io
import unittest

from fortigate_extract.web import create_app


_SAMPLE_CONFIG = b"""
config system interface
    edit "port1"
        set ip 192.0.2.1 255.255.255.0
    next
end
"""


class WebUITest(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app(
            {
                "TESTING": True,
            }
        )
        self.client = self.app.test_client()

    def test_index_renders_without_missing_partials(self):
        response = self.client.get("/")

        self.assertEqual(
            200,
            response.status_code,
        )

        html = response.get_data(
            as_text=True
        )

        self.assertIn(
            "FortiGate Excel Report",
            html,
        )
        self.assertIn(
            'id="btn-extract-excel"',
            html,
        )
        self.assertNotIn(
            "partials/exports.html",
            html,
        )
        self.assertNotIn(
            "Live migration",
            html,
        )
        self.assertNotIn(
            "FortiGate source.",
            html,
        )
        self.assertNotIn(
            "The workbook preserves the original report layout",
            html,
        )
        self.assertNotIn(
            "inventory-summary-copy",
            html,
        )
        self.assertNotIn(
            "AT A GLANCE",
            html,
        )
        self.assertNotIn(
            "Configuration overview",
            html,
        )
        self.assertNotIn(
            "Source extraction · derived views · validation · Excel",
            html,
        )
        self.assertIn(
            'id="validation-error-count"',
            html,
        )
        self.assertIn(
            'id="validation-warning-count"',
            html,
        )

    def test_preview_accepts_fortigate_upload(self):
        response = self.client.post(
            "/api/preview",
            data={
                "file": (
                    io.BytesIO(
                        _SAMPLE_CONFIG
                    ),
                    "sample.conf",
                )
            },
            content_type="multipart/form-data",
        )

        self.assertEqual(
            200,
            response.status_code,
        )

        data = response.get_json()

        self.assertTrue(
            data["success"]
        )
        self.assertEqual(
            1,
            data["objects"]["interfaces"],
        )

    def test_excel_endpoint_returns_xlsx(self):
        response = self.client.post(
            "/api/extract/excel",
            data={
                "file": (
                    io.BytesIO(
                        _SAMPLE_CONFIG
                    ),
                    "sample.conf",
                )
            },
            content_type="multipart/form-data",
        )

        self.assertEqual(
            200,
            response.status_code,
        )
        self.assertEqual(
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            response.mimetype,
        )
        self.assertTrue(
            response.data.startswith(
                b"PK"
            )
        )


if __name__ == "__main__":
    unittest.main()
