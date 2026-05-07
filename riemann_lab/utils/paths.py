"""Robust path helpers for source data and generated outputs.

Source-controlled files live under the repository root.  Generated outputs are
kept under ``artifacts/`` by default so that computed data is not confused with
validated mathematical reference data.
"""

from __future__ import annotations

from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = PACKAGE_ROOT.parent
LEGACY_ZERO_DATA_PATH = REPOSITORY_ROOT / "compute_zeros" / "data" / "known_zeros.txt"
ARTIFACTS_DIR = REPOSITORY_ROOT / "artifacts"


def repository_path(*parts: str) -> Path:
    """Return a path under the repository root."""

    return REPOSITORY_ROOT.joinpath(*parts)


def artifacts_path(*parts: str, create_parent: bool = True) -> Path:
    """Return a path under ``artifacts/`` and optionally create its parent."""

    path = ARTIFACTS_DIR.joinpath(*parts)
    if create_parent:
        path.parent.mkdir(parents=True, exist_ok=True)
    return path


def resolve_output_path(path: str | Path | None, *default_parts: str) -> Path:
    """Resolve an optional user output path or a default artifact path."""

    if path is None:
        return artifacts_path(*default_parts)
    resolved = Path(path).expanduser().resolve()
    resolved.parent.mkdir(parents=True, exist_ok=True)
    return resolved
