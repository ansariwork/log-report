import json
from pathlib import Path

REPORT_PATH = Path("/app/out.json")

def test_criterion_1_file_exists_and_valid_json():
    """Criterion 1: The file /app/out.json exists and contains valid JSON."""
    assert REPORT_PATH.exists(), "out.json is missing"
    try:
        data = json.loads(REPORT_PATH.read_text())
        assert isinstance(data, dict)
    except json.JSONDecodeError:
        assert False, "out.json is not valid JSON"

def test_criterion_2_total_requests():
    """Criterion 2: `total_requests` is the exact count of log entries in the file."""
    data = json.loads(REPORT_PATH.read_text())
    assert data.get("total_requests") == 6

def test_criterion_3_unique_ips():
    """Criterion 3: `unique_ips` is the exact count of distinct IP addresses that made requests."""
    data = json.loads(REPORT_PATH.read_text())
    assert data.get("unique_ips") == 3

def test_criterion_4_top_path():
    """Criterion 4: `top_path` is the URL path (e.g. `/index.html`) with the highest request count."""
    data = json.loads(REPORT_PATH.read_text())
    assert data.get("top_path") == "/index.html"
