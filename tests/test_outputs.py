import json
from pathlib import Path

REPORT_PATH = Path("/app/out.json")

def test_report_exists():
    assert REPORT_PATH.exists(), "out.json is missing"

def test_report_content():
    # Load and parse the report
    try:
        data = json.loads(REPORT_PATH.read_text())
    except json.JSONDecodeError:
        assert False, "out.json is not valid JSON"
        
    assert isinstance(data, dict), "root JSON element should be a dictionary"
    
    # Check the required stats based on access.log
    assert data.get("total_requests") == 6
    assert data.get("unique_ips") == 3
    assert data.get("top_path") == "/index.html"
