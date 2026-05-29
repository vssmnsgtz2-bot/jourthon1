from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse

root = Path('/home/ubuntu/jourthon_static_site')
html_files = sorted(root.glob('*.html'))
errors = []

class Parser(HTMLParser):
    def __init__(self, page):
        super().__init__()
        self.page = page
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ('href', 'src'):
            if key not in attrs:
                continue
            value = attrs[key].strip()
            if not value or value.startswith(('#', 'mailto:', 'tel:', 'http://', 'https://')):
                continue
            parsed = urlparse(value)
            path_part = parsed.path
            if not path_part:
                continue
            target = (root / path_part).resolve()
            if root.resolve() not in target.parents and target != root.resolve():
                errors.append(f'{self.page.name}: {value} escapes root')
            elif not target.exists():
                errors.append(f'{self.page.name}: missing {value}')

for html in html_files:
    parser = Parser(html)
    parser.feed(html.read_text(encoding='utf-8'))

if errors:
    print('FAILED')
    for error in errors:
        print(error)
    raise SystemExit(1)

print(f'PASSED: {len(html_files)} HTML files checked; all local links/assets exist.')
