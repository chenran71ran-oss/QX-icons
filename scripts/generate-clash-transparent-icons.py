"""Render transparent Clash brand marks; keep QX's circular assets separate."""
from io import BytesIO
from pathlib import Path
import re

import cairosvg
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
VECTOR = ROOT / 'icons/sources/clash-transparent'
DEST = ROOT / 'icons/clash/apps'
NAMES = ['ChatGPT', 'Claude', 'Gemini', 'Muse', 'Manus', 'Grok', 'Google']


def render(name, light=False):
    source = ROOT/'icons/sources/Muse-official.svg' if name == 'Muse' else VECTOR/(name+'.svg')
    text = re.sub(r' style="[^"]*"', '', source.read_text())
    # Use colored OpenAI branding and light monochrome marks on dark dashboards.
    color = '#10A37F' if name == 'ChatGPT' else ('#333333' if light else '#F3F4F6')
    text = text.replace('currentColor', color)
    image = Image.open(BytesIO(cairosvg.svg2png(bytestring=text.encode(), output_width=2048, output_height=2048))).convert('RGBA')
    image = image.crop(image.getchannel('A').getbbox())
    image.thumbnail((1720, 1720), Image.Resampling.LANCZOS)
    canvas = Image.new('RGBA', (2048, 2048), (0, 0, 0, 0))
    canvas.alpha_composite(image, ((2048-image.width)//2, (2048-image.height)//2))
    return canvas.resize((512, 512), Image.Resampling.LANCZOS)


def main():
    DEST.mkdir(parents=True, exist_ok=True)
    for name in NAMES:
        render(name).save(DEST/(name+'-transparent-v1.png'), optimize=True)
    (DEST/'light').mkdir(exist_ok=True)
    for name in ['Manus', 'Grok']:
        render(name, light=True).save(DEST/'light'/(name+'-transparent-v1.png'), optimize=True)


if __name__ == '__main__':
    main()
