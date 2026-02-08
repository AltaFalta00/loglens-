from __future__ import annotations

import re
from datetime import datetime
from typing import Iterable

from .types import LogEvent


# Supports formats like:
# 2026-02-08 12:34:56 INFO Something happened
# 2026-02-08T12:34:56Z ERROR Timeout
_PATTERN = re.compile(
    r"^(?P<ts>\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}(?:Z)?)\s+"
    r"(?P<level>[A-Z]+)\s+"
    r"(?P<msg>.*)$"
)


def parse_line(line: str) -> LogEvent:
    raw = line.rstrip("\n")
    m = _PATTERN.match(raw)

    if not m:
        return LogEvent(
            ts=None,
            level="UNKNOWN",
            message=raw,
            raw=raw,
        )

    ts = _parse_timestamp(m.group("ts"))
    level = m.group("level")
    msg = m.group("msg")

    return LogEvent(
        ts=ts,
        level=level,
        message=msg,
        raw=raw,
    )



def _parse_timestamp(value: str) -> datetime | None:
    try:
        if value.endswith("Z"):
            value = value.replace("T", " ").removesuffix("Z")
        else:
            value = value.replace("T", " ")
        return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return None


def iter_events(lines: Iterable[str]) -> Iterable[LogEvent]:
    for line in lines:
        yield parse_line(line)
