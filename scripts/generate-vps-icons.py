#!/usr/bin/env python3
"""Reproducible RackNerd aliases and temporary RackSmart server glyphs."""
from pathlib import Path
from shutil import copyfile
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
SIZE = 576
WHITE = (255, 255, 255, 255)

def racksmart_glyph():
    im = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for y in (112, 236, 360):
        d.rounded_rectangle((88, y, 405, y + 86), radius=22, outline=WHITE, width=20)
        d.ellipse((119, y + 31, 143, y + 55), fill=WHITE)
        d.rounded_rectangle((168, y + 36, 282, y + 50), radius=7, fill=WHITE)
    # Lightning at the right edge; transparent gaps remain readable as a QX mask.
    d.polygon([(423, 161), (346, 310), (414, 310), (365, 462), (506, 267), (438, 267), (481, 161)], fill=WHITE)
    return im

def save(im, rel, size):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    im.resize((size, size), Image.Resampling.LANCZOS).save(p, 'PNG', optimize=True)

def main():
    aliases = {
        'icons/subscriptions/RN-VPS.png': ['icons/subscriptions/RackNerd.png'],
        'icons/qx/subscriptions/RN-VPS-circle-v2.png': ['icons/qx/subscriptions/RackNerd.png', 'icons/qx/subscriptions/RackNerd-circle-v2.png'],
        'icons/qx/proxy/RN-VPS.png': ['icons/qx/proxy/RackNerd.png'],
    }
    for source, destinations in aliases.items():
        for dest in destinations:
            target = ROOT / dest
            target.parent.mkdir(parents=True, exist_ok=True)
            copyfile(ROOT / source, target)
    glyph = racksmart_glyph()
    save(glyph, 'icons/qx/proxy/RackSmart.png', 144)
    color = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
    ImageDraw.Draw(color).ellipse((28, 28, SIZE-29, SIZE-29), fill=(35, 104, 218, 255))
    inner = glyph.resize((440, 440), Image.Resampling.LANCZOS)
    color.alpha_composite(inner, (68, 68))
    save(color, 'icons/subscriptions/RackSmart.png', 432)
    save(color, 'icons/qx/subscriptions/RackSmart.png', 108)
    save(color, 'icons/qx/subscriptions/RackSmart-circle-v2.png', 108)

if __name__ == '__main__':
    main()
