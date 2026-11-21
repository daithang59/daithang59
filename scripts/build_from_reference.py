#!/usr/bin/env python3
"""Fetch Kiên's original SVGs and personalize only header + certification imagery.

Requires permission from the original creator before publishing modified/copy assets.
Original SVG animation and layout remain unchanged; only name, typing length,
and 5 AWS badge raster payloads are replaced.
"""
from __future__ import annotations

import argparse
import base64
import io
import re
import sys
from pathlib import Path
from urllib.request import Request, urlopen

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"
BASE = "https://raw.githubusercontent.com/Kien-devops/Kien-devops/main/"
SOURCE = "https://github.com/Kien-devops/Kien-devops"

# Exact sequence used by Kiên's five-badge trophy case:
# Cloud Practitioner, Solutions Architect, CloudOps, Developer, DevOps Professional.
# Replace artwork in the SAME positions with Dai Thang's five real credentials.
BADGES = [
    ("AWS Certified Cloud Practitioner", "https://images.credly.com/images/00634f82-b07f-4bbd-a6bb-53de397fc3a6/image.png"),
    ("AWS Certified Solutions Architect – Associate", "https://images.credly.com/images/0e284c3f-5164-4b21-8660-0d84737941bc/image.png"),
    ("AWS Certified CloudOps Engineer – Associate", "https://images.credly.com/images/88a6405e-0f26-442a-95ed-f9b9db4c857e/blob"),
    ("AWS Certified Developer – Associate", "https://images.credly.com/images/b9feab85-1a43-4f6c-99a5-631b88d5461b/image.png"),
    ("AWS Certified AI Practitioner", "https://images.credly.com/images/4d4693bb-530e-4bca-9327-de07f3aa2348/image.png"),
]


def download(url: str) -> bytes:
    request = Request(url, headers={"User-Agent": "DaiThang-GitHub-README/1.0", "Accept": "*/*"})
    with urlopen(request, timeout=25) as resp:
        result = resp.read()
    if not result:
        raise RuntimeError(f"Empty response for {url}")
    return result


def official_badge_payload(url: str, width: int, height: int) -> str:
    with Image.open(io.BytesIO(download(url))) as photo:
        image = photo.convert("RGBA")
    # Preserve the real AWS/Credly badge proportions; cut transparent padding only.
    bbox = image.getchannel("A").getbbox()
    if bbox:
        image = image.crop(bbox)
    image.thumbnail((width, height), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    canvas.alpha_composite(image, ((width - image.width)//2, (height - image.height)//2))
    buf = io.BytesIO()
    canvas.save(buf, format="PNG", optimize=True)
    return base64.b64encode(buf.getvalue()).decode("ascii")


def change_header(svg: str) -> str:
    if "Nguyen Trung Kien" not in svg:
        raise RuntimeError("Original header changed: can't locate the original name.")
    svg = svg.replace("Nguyen Trung Kien", "Dai Thang")
    # No redesign: only typing clip width, cursor end point and X position are changed
    # so the shorter name stays centered and the cursor does not overshoot.
    svg = svg.replace('steps(17)', 'steps(9)')
    svg = svg.replace('400px', '220px')
    svg = svg.replace('x="252"', 'x="320"')
    svg = svg.replace('x1="252"', 'x1="320"').replace('x2="252"', 'x2="320"')
    svg = svg.replace('DEVOPS • CLOUD • SECURITY', 'CLOUD • DEVOPS • AWS')
    return svg


IMAGE_RE = re.compile(r'(<image\b[^>]*?\bhref="data:image/[^;]+;base64,)([^\"]+)(")', re.S)


def change_certifications(svg: str) -> str:
    originals = list(IMAGE_RE.finditer(svg))
    if len(originals) != 5:
        raise RuntimeError(f"Expected 5 embedded original badges; found {len(originals)}. Original source may have changed.")
    assembled = []
    pos = 0
    for i, m in enumerate(originals):
        assembled.append(svg[pos:m.start()])
        image_tag_start = m.group(1)
        # Source's embed slots are 119x138 in the reference layout.
        tag_prefix = svg[max(0, svg.rfind('<image',0,m.start())):m.start()]
        width = int(re.search(r'width="(\d+)"', tag_prefix).group(1)) if re.search(r'width="(\d+)"', tag_prefix) else 119
        height = int(re.search(r'height="(\d+)"', tag_prefix).group(1)) if re.search(r'height="(\d+)"', tag_prefix) else 138
        payload = official_badge_payload(BADGES[i][1], width, height)
        # Copy original tag, CSS, glow, sizes and animation timing unchanged.
        assembled.append(image_tag_start + payload + m.group(3))
        pos = m.end()
        print(f"  Badge {i+1}/5: {BADGES[i][0]} ({width}x{height})")
    assembled.append(svg[pos:])
    return "".join(assembled)


def main() -> None:
    parser = argparse.ArgumentParser(description="Match Kiên's original README SVG design and animation precisely")
    parser.add_argument("--permission-confirmed", action="store_true", help="Confirm you have permission to reuse/adapt the original assets")
    args = parser.parse_args()
    if not args.permission_confirmed:
        parser.error("Confirm usage rights with the SVG creator first, then pass --permission-confirmed")
    OUT.mkdir(parents=True, exist_ok=True)
    for name in ("header.svg", "philosophy-flow.svg", "aws-certifications.svg", "tech-stack.svg"):
        data = download(BASE + name)
        svg = data.decode("utf-8-sig")
        if "<svg" not in svg or "</svg>" not in svg:
            raise RuntimeError(f"Unexpected SVG response from {name}")
        if name == "header.svg":
            svg = change_header(svg)
        elif name == "aws-certifications.svg":
            svg = change_certifications(svg)
        target = OUT / name
        target.write_text(svg, encoding="utf-8")
        print(f"Saved {target.relative_to(ROOT)} ({target.stat().st_size:,} bytes)")
    # After downloading, stop hotlinking the reference assets; serve local exact copies.
    readme = ROOT / "README.md"
    page = readme.read_text(encoding="utf-8")
    page = page.replace(BASE + "philosophy-flow.svg", "assets/philosophy-flow.svg")
    page = page.replace(BASE + "tech-stack.svg", "assets/tech-stack.svg")
    readme.write_text(page, encoding="utf-8")
    print("Complete. Workflow and tooling are unmodified source SVGs; the others retain original animation and layout.")


if __name__ == "__main__":
    main()
