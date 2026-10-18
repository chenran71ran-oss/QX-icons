#!/usr/bin/env python3
"""Reproducible VPS icons: server racks with a shield or lightning accent."""
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

def racknerd_glyph():
    im = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for y in (112, 236, 360):
        d.rounded_rectangle((88, y, 405, y + 86), radius=22, outline=WHITE, width=20)
        d.ellipse((119, y + 31, 143, y + 55), fill=WHITE)
        d.rounded_rectangle((168, y + 36, 282, y + 50), radius=7, fill=WHITE)
    # A compact shield distinguishes RN from RackSmart's lightning.
    d.polygon([(422, 235), (512, 268), (497, 379), (422, 449), (347, 379), (332, 268)], fill=WHITE)
    d.line([(380, 335), (411, 366), (467, 306)], fill=(20, 153, 142, 255), width=23, joint='curve')
    return im

def save(im, rel, size):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    im.resize((size, size), Image.Resampling.LANCZOS).save(p, 'PNG', optimize=True)

def main():
    aliases = {
        'icons/qx/proxy/RN-VPS.png': ['icons/qx/proxy/RackNerd.png'],
    }
    for source, destinations in aliases.items():
        for dest in destinations:
            target = ROOT / dest
            target.parent.mkdir(parents=True, exist_ok=True)
            copyfile(ROOT / source, target)
    rn_color = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
    ImageDraw.Draw(rn_color).ellipse((28, 28, SIZE-29, SIZE-29), fill=(20, 153, 142, 255))
    rn_color.alpha_composite(racknerd_glyph().resize((440, 440), Image.Resampling.LANCZOS), (68, 68))
    save(rn_color, 'icons/subscriptions/RackNerd.png', 432)
    save(rn_color, 'icons/qx/subscriptions/RackNerd.png', 108)
    save(rn_color, 'icons/qx/subscriptions/RackNerd-circle-v2.png', 108)
    save(rn_color, 'icons/qx/subscriptions/RackNerd-circle-v3.png', 108)
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
