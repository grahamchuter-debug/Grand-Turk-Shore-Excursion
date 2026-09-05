#!/usr/bin/env python3
"""Download licensed Unsplash images for missing Grand Turk assets. Skips existing large files."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "images"

# Owned photography — never overwrite if present and large enough.
OWNED: frozenset[str] = frozenset({
    "hero-grand-turk.png",
    "gibbs-cay-stingray.png",
    "grand-turk-snorkelling.png",
    "grand-turk-intro.png",
    "grand-turk-beach-breaks.png",
    "grand-turk-beaches.png",
    "grand-turk-island-tours.png",
})

# filename, unsplash photo id, width
DOWNLOADS: list[tuple[str, str, int]] = [
    ("best-grand-turk-excursions.png", "Q0HR_nrDkB8", 1600),
    ("one-day-grand-turk.png", "YZ8Jc6TiH2A", 1600),
    ("governors-beach.png", "BUIEgc7J0eo", 1600),
    ("grand-turk-golf-cart.png", "PsgyWVeJjOA", 1600),
    ("grand-turk-private-tours.png", "eOpewngf68w", 1600),
    ("grand-turk-family.png", "KMn4VEeEPR8", 1600),
    ("grand-turk-faq.png", "rDEOVtE7vOs", 1600),
    ("grand-turk-cruise-port.png", "vYXrNeIpm3w", 1600),
]


def download(filename: str, slug: str, width: int) -> bool:
    dest = IMAGES / filename
    if dest.exists() and dest.stat().st_size > 20_000:
        print(f"  skip existing {filename} ({dest.stat().st_size // 1024} KB)")
        return True
    url = f"https://unsplash.com/photos/{slug}/download?force=true&w={width}"
    print(f"  {filename} <- {slug}")
    result = subprocess.run(
        ["curl", "-fsSL", "-L", "-o", str(dest), url],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"    FAILED: {result.stderr.strip()}", file=sys.stderr)
        return False
    size = dest.stat().st_size
    if size < 10_000:
        print(f"    WARNING: small file ({size} bytes)", file=sys.stderr)
        return False
    print(f"    OK ({size // 1024} KB)")
    return True


def main() -> None:
    IMAGES.mkdir(parents=True, exist_ok=True)
    print("Fetching Grand Turk licensed images (skip owned/existing)…")
    print(f"  Owned protected: {', '.join(sorted(OWNED))}")
    failed = 0
    for filename, slug, width in DOWNLOADS:
        if filename in OWNED:
            continue
        if not download(filename, slug, width):
            failed += 1
    if failed:
        raise SystemExit(f"{failed} download(s) failed.")
    print("Done. See images/ATTRIBUTION.md")


if __name__ == "__main__":
    main()
