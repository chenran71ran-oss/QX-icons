"""Export the official Muse vector mark without App Store glass/shadow padding."""
from io import BytesIO
from pathlib import Path
import json
import re

import cairosvg
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'icons/sources/Muse-official.svg'


def render(size, circular=False):
    scale = 4
    large = size * scale
    # CairoSVG does not implement CSS Color 4 display-p3. Keep the official
    # sRGB stop-color attributes instead of letting unsupported styles go black.
    svg = re.sub(r' style="[^"]*"', '', SOURCE.read_text())
    logo = Image.open(BytesIO(cairosvg.svg2png(
        bytestring=svg.encode(), output_width=2048, output_height=2048))).convert('RGBA')
    logo = logo.crop(logo.getchannel('A').getbbox())
    # Larger visible mark; retain its aspect ratio and the complete path.
    extent = round(large * .74)
    logo.thumbnail((extent, extent), Image.Resampling.LANCZOS)
    image = Image.new('RGBA', (large, large), (255, 255, 255, 255))
    image.alpha_composite(logo, ((large-logo.width)//2, (large-logo.height)//2))
    if circular:
        mask = Image.new('L', image.size)
        pad = 5*scale
        ImageDraw.Draw(mask).ellipse((pad, pad, large-pad-1, large-pad-1), fill=255)
        image.putalpha(mask)
    return image.resize((size, size), Image.Resampling.LANCZOS)


def main():
    render(512).save(ROOT/'icons/apps/Muse.png', optimize=True)
    circle = render(108, True)
    for name in ['Muse.png', 'Muse-circle-v2.png', 'Muse-circle-v3.png']:
        circle.save(ROOT/'icons/qx/apps'/name, optimize=True)
    (ROOT/'icons/sources/Muse-source.json').write_text(json.dumps({
        'source': 'https://muse.ai/images/landing/brand/muse-logo.svg',
        'verified_on': '2026-10-27',
        'render': 'Official SVG; white circle; no JPEG intermediate; supersampled PNG',
        'qx': 'icons/qx/apps/Muse-circle-v3.png',
        'clash': 'icons/apps/Muse.png',
    }, indent=2)+'\n')


if __name__ == '__main__':
    main()
