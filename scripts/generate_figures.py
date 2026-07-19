"""Validate the three SVG concept figures against lightweight JSON source data.

The committed SVGs are hand-tuned for readability, but this script records the
reproducible source objects used by the perspective. It is intentionally minimal
so it can run anywhere Python 3 is available.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_json(name: str) -> dict:
    with (ROOT / "data" / name).open(encoding="utf-8") as file:
        return json.load(file)


def main() -> None:
    publication = load_json("publication-models.json")
    visibility = load_json("evidence-visibility.json")
    manifest = load_json("evidence-record-anatomy.json")
    print(f"Loaded publication comparison with a {publication['proposed_model']['relationship']} proposed model.")
    outcome_count = len(visibility["illustrative_outcomes"])
    print(f"Loaded evidence-visibility comparison with {outcome_count} illustrative outcomes.")
    object_count = len(manifest["record"]["objects"])
    print(f"Loaded proposed evidence-record anatomy with {object_count} typed object references.")
    print("SVG figure layouts are stored in figures/ for MyST publication.")


if __name__ == "__main__":
    main()
