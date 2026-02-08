from __future__ import annotations

import argparse
from pathlib import Path

from .parsing import iter_events


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="loglens",
        description="Parse and analyze log files.",
    )
    parser.add_argument(
        "path",
        type=Path,
        help="Path to a log file",
    )
    args = parser.parse_args()

    path: Path = args.path
    if not path.exists() or not path.is_file():
        raise SystemExit(f"Not a file: {path}")

    with path.open("r", encoding="utf-8", errors="replace") as f:
        for event in iter_events(f):
            print(f"{event.level:8} {event.message}")


if __name__ == "__main__":
    main()
