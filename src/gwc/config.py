"""Load optional gwc configuration from ./.gwcrc."""
from __future__ import annotations

import tomllib
from pathlib import Path


def load_config(path: Path | None = None) -> dict:
    path = path or Path(".gwcrc")
    if not path.exists():
        return {}
    with path.open("rb") as f:
        return tomllib.load(f)
