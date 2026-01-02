import os
from datetime import datetime
import analyzer


def test_parse_text_log_valid():
    line = "2025-01-01 10:00:00 ERROR payment host2 Payment failed"
    result = analyzer.parse_text_log(line)

    assert result["level"] == "ERROR"
    assert result["service"] == "payment"
    assert result["host"] == "host2"
    assert result["message"] == "Payment failed"
    assert isinstance(result["timestamp"], datetime)


def test_parse_text_log_invalid():
    assert analyzer.parse_text_log("INVALID LINE") is None


def test_read_logs():
    logs = analyzer.read_logs()
    assert len(logs) > 0
