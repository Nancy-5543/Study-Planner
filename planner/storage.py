import json
from pathlib import Path


DATA_FILE = Path(__file__).parent.parent / "data" / "study_data.json"


def load_data():
    """Load study data from the JSON file."""

    if not DATA_FILE.exists():
        return {
            "tasks": [],
            "revisions": [],
            "sessions": []
        }

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_data(data):
    """Save study data to the JSON file."""

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)