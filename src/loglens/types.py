from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class LogEvent:
    ts: datetime | None
    level: str
    message: str
    raw: str
