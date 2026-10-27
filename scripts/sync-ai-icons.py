"""Sync official AI artwork and produce the repository's existing client formats."""
from io import BytesIO
from pathlib import Path
import datetime
import json
import urllib.request

from PIL import Image, ImageChops, ImageDraw, ImageOps

ROOT = Path(__file__).resolve().parents[1]
APPS = {
    'Muse': (6760173601, 'com.facebook.hatch'),
    'Manus': (6740909540, 'tech.butterfly.app'),
    'Grok': (6670324846, 'ai.x.GrokApp'),
    'Cue': (6808613358, 'ai.manus.agents'),
    'GrokBot': (6794501026, 'co.anysphere.sand'),
}


def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'QX-icons/1.0'})
    with urllib.request.urlopen(req, timeout=30) as response:
        return response.read()


def main():
    app_dir, qx_dir = ROOT / 'icons/apps', ROOT / 'icons/qx/apps'
    app_dir.mkdir(parents=True, exist_ok=True)
    qx_dir.mkdir(parents=True, exist_ok=True)
    metadata = {'source': 'Apple iTunes Lookup API', 'country': 'us',
                'synced_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'apps': {}}
    # Validate all identities before replacing any asset.
    fetched = []
    for name, (track_id, bundle_id) in APPS.items():
        results = json.loads(get(f'https://itunes.apple.com/lookup?id={track_id}&country=us'))['results']
        if not results or results[0].get('bundleId') != bundle_id:
            raise RuntimeError(f'Unexpected App Store identity for {name}')
        item = results[0]
        artwork = item.get('artworkUrl512') or item['artworkUrl100']
        image = Image.open(BytesIO(get(artwork))).convert('RGBA')
        image.load()
        fetched.append((name, item, artwork, image))
    for name, item, artwork, image in fetched:
        full = ImageOps.fit(image, (512, 512), method=Image.Resampling.LANCZOS)
        full.save(app_dir / f'{name}.png', 'PNG', optimize=True)
        full.convert('RGB').save(app_dir / f'{name}.jpg', 'JPEG', quality=95)
        # Same 108px, 5px inset circular mask as sync-icons.yml.
        circle = ImageOps.fit(image, (108, 108), method=Image.Resampling.LANCZOS)
        mask = Image.new('L', (432, 432), 0)
        ImageDraw.Draw(mask).ellipse((20, 20, 411, 411), fill=255)
        mask = mask.resize((108, 108), Image.Resampling.LANCZOS)
        circle.putalpha(ImageChops.multiply(circle.getchannel('A'), mask))
        for filename in [f'{name}.png', f'{name}-circle-v2.png']:
            circle.save(qx_dir / filename, 'PNG', optimize=True)
        metadata['apps'][name] = {key: item.get(key) for key in
            ['trackId', 'trackName', 'sellerName', 'bundleId', 'trackViewUrl', 'version']}
        metadata['apps'][name]['artworkUrl512'] = artwork
        print(f'Synced {name}: Clash PNG 512px / QX circular RGBA 108px')
    (app_dir / 'ai-appstore-meta.json').write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
