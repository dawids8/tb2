import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def _load_report():
    return json.loads(REPORT_PATH.read_text())


# Criterion 1: /app/report.json exists and contains valid JSON.
def test_report_is_valid_json():
    assert REPORT_PATH.exists(), "no report.json found"
    _load_report()


# Criterion 2: total_requests equals the total number of request lines.
def test_total_requests():
    assert _load_report()["total_requests"] == 6


# Criterion 3: unique_ips equals the number of distinct client IPs.
def test_unique_ips():
    assert _load_report()["unique_ips"] == 3


# Criterion 4: top_path equals the most frequently requested path.
def test_top_path():
    assert _load_report()["top_path"] == "/index.html"
