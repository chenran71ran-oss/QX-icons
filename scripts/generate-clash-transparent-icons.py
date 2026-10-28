"""Render transparent Clash brand marks; keep QX's circular assets separate."""
from io import BytesIO
from pathlib import Path
import re
import json

import cairosvg
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
VECTOR = ROOT / 'icons/sources/clash-transparent'
DEST = ROOT / 'icons/clash/apps'
NAMES = ['ChatGPT', 'Claude', 'Gemini', 'Muse', 'Manus', 'Grok', 'Google']
APP_MANIFEST = VECTOR / 'apps-sources.json'


def render(name, light=False):
    source = ROOT/'icons/sources/Muse-official.svg' if name == 'Muse' else VECTOR/(name+'.svg')
    text = re.sub(r' style="[^"]*"', '', source.read_text())
    # White OpenAI branding and light monochrome marks on dark dashboards.
    color = '#333333' if light else '#F3F4F6'
    text = text.replace('currentColor', color)
    return export(text)


def export(text):
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
    for name in ['ChatGPT', 'Manus', 'Grok']:
        render(name, light=True).save(DEST/'light'/(name+'-transparent-v1.png'), optimize=True)
    # Versioned URL bypasses the cached green ChatGPT export.
    render('ChatGPT').save(DEST/'ChatGPT-transparent-v2.png', optimize=True)
    render('ChatGPT', light=True).save(DEST/'light'/'ChatGPT-transparent-v2.png', optimize=True)
    if APP_MANIFEST.exists():
        for name, spec in json.loads(APP_MANIFEST.read_text())['icons'].items():
            text = (ROOT/spec['file']).read_text()
            # Simple Icons sources inherit a fill; SVGL TikTok keeps its cyan/red paths.
            fill = spec['color']
            if name == 'Instagram':
                gradient = '<defs><linearGradient id="instagram-brand" x1="0" y1="1" x2="1" y2="0"><stop stop-color="#FEDA75"/><stop offset=".3" stop-color="#FA7E1E"/><stop offset=".55" stop-color="#D62976"/><stop offset=".8" stop-color="#962FBF"/><stop offset="1" stop-color="#4F5BD5"/></linearGradient></defs>'
                text = text.replace('</title>', '</title>'+gradient)
                fill = 'url(#instagram-brand)'
            text = text.replace('<svg ', '<svg fill="'+fill+'" ', 1)
            export(text).save(DEST/(name+'-transparent-v1.png'), optimize=True)
            if spec.get('light_color'):
                text = text.replace('fill="'+fill+'"', 'fill="'+spec['light_color']+'"', 1)
                export(text).save(DEST/'light'/(name+'-transparent-v1.png'), optimize=True)


if __name__ == '__main__':
    main()
