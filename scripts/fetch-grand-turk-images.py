#!/usr/bin/env python3
"""Download hero and content images from Unsplash (Unsplash License)."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMAGES = ROOT / "images"

# Site-provided; skipped by fetch (see images/ATTRIBUTION.md).
CUSTOM_IMAGES: frozenset[str] = frozenset({
    "hero-grand-turk.png",
    "grand-turk-cruise-port.png",
    "gibbs-cay-stingray.png",
    "grand-turk-snorkelling.png",
    "grand-turk-intro.png",
    "grand-turk-faq.png",
    "grand-turk-beach-breaks.png",
    "grand-turk-beaches.png",
    "grand-turk-island-tours.png",
})

DOWNLOADS: list[tuple[str, str, int]] = [
    ("best-grand-turk-excursions.png", "Q0HR_nrDkB8", 1920),
    ("one-day-grand-turk.png", "YZ8Jc6TiH2A", 1920),
    ("grand-turk-snorkelling.png", "uTgKYNhuKOk", 1920),
    ("grand-turk-beach-breaks.png", "Q0HR_nrDkB8", 1920),
    ("governors-beach.png", "BUIEgc7J0eo", 1920),
    ("grand-turk-island-tours.png", "vYXrNeIpm3w", 1920),
    ("grand-turk-golf-cart.png", "PsgyWVeJjOA", 1920),
    ("grand-turk-lighthouse.png", "WOyBhxyB8KI", 1920),
    ("grand-turk-private-tours.png", "PsgyWVeJjOA", 1920),
    ("grand-turk-family.png", "BUIEgc7J0eo", 1920),
    ("grand-turk-beaches.png", "Q0HR_nrDkB8", 1920),
    ("grand-turk-intro.png", "YZ8Jc6TiH2A", 1920),
]


def download(filename: str, slug: str, width: int) -> bool:
    dest = IMAGES / filename
    url = f"https://unsplash.com/photos/{slug}/download?force=true&w={width}"
    print(f"  {filename} <- {slug}")
    result = subprocess.run(
        ["curl", "-fsSL", "-o", str(dest), url],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"    FAILED: {result.stderr.strip()}", file=sys.stderr)
        return False
    size = dest.stat().st_size
    if size < 10_000:
        print(f"    WARNING: small file ({size} bytes)", file=sys.stderr)
    print(f"    OK ({size // 1024} KB)")
    return True


def main() -> None:
    IMAGES.mkdir(parents=True, exist_ok=True)
    print("Downloading Grand Turk images from Unsplash…")
    if CUSTOM_IMAGES:
        print(f"  Skipping custom (add your own): {', '.join(sorted(CUSTOM_IMAGES))}")
    failed = 0
    for filename, slug, width in DOWNLOADS:
        if filename in CUSTOM_IMAGES:
            continue
        if not download(filename, slug, width):
            failed += 1
    if failed:
        raise SystemExit(f"{failed} download(s) failed.")
    print("Done.")


if __name__ == "__main__":
    main()
