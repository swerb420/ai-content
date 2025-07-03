"""Local JSON-based storage for project data."""

import json
from pathlib import Path

BASE_FILE = Path("data.json")


def save_record(record: dict) -> None:
    data = load_data()
    data.append(record)
    BASE_FILE.write_text(json.dumps(data, indent=2))


def load_data() -> list[dict]:
    if BASE_FILE.exists():
        return json.loads(BASE_FILE.read_text())
    return []
