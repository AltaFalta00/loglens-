from datetime import datetime

from loglens.parsing import parse_line


def test_parse_valid_line():
    line = "2026-02-08 12:34:56 INFO Something happened"
    event = parse_line(line)

    assert event.level == "INFO"
    assert event.message == "Something happened"
    assert event.ts == datetime(2026, 2, 8, 12, 34, 56)
    assert event.raw == line


def test_parse_unknown_line():
    line = "this is not a valid log line"
    event = parse_line(line)

    assert event.level == "UNKNOWN"
    assert event.ts is None
    assert event.message == line
