from pathlib import Path

# Project paths
PACKAGE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = PACKAGE_DIR.parent.parent
OUTPUT_DIR = PROJECT_ROOT / "output"

# Web application
APP_HOST = "127.0.0.1"
APP_PORT = 5000
DEBUG = False

# Upload handling
ALLOWED_EXTENSIONS = {".conf", ".cfg", ".txt"}
MAX_UPLOAD_SIZE = 20 * 1024 * 1024  # 20 MB

# Excel export
DEFAULT_EXCEL_FILENAME = "fortigate_inventory.xlsx"

# Extraction
DEFAULT_SOURCE_CONTEXT = "root"


def is_allowed_file(filename: str) -> bool:
    """Return True when the uploaded file extension is supported."""
    return Path(filename).suffix.lower() in ALLOWED_EXTENSIONS