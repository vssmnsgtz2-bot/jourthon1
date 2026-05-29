from pathlib import Path
from bs4 import BeautifulSoup
import re

root = Path('/home/ubuntu/jourthon_static_site')
pages = sorted(root.glob('*.html'))
risk_patterns = [
    r'\bdrug\b', r'\bpharmaceutical\b', r'\bmedicine\b', r'\bpatient\b',
    r'clinical treatment', r'\btherapy\b', r'\btherapeutic\b', r'\bpharmacy\b',
    r"we don't just manufacture", r'your next supplement brand', r'wellness brands',
    r'launch partner', r'Compliance Fast Track', r'New Brand Launch', r'Market Entry Support'
]
print('# Full Site Audit\n')
for p in pages:
    soup = BeautifulSoup(p.read_text(encoding='utf-8'), 'html.parser')
    title = soup.title.get_text(' ', strip=True) if soup.title else ''
    h1 = [h.get_text(' ', strip=True) for h in soup.find_all('h1')]
    h2 = [h.get_text(' ', strip=True) for h in soup.find_all('h2')]
    footer = soup.find('footer')
    footer_text = footer.get_text(' ', strip=True) if footer else ''
    links = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        if href.endswith('.html') or '.html#' in href or href.startswith('#'):
            links.append((a.get_text(' ', strip=True), href))
    text = soup.get_text(' ', strip=True)
    risks = []
    for pat in risk_patterns:
        for m in re.finditer(pat, text, flags=re.I):
            s=max(0,m.start()-70); e=min(len(text),m.end()+90)
            risks.append((pat, text[s:e]))
    print(f'## {p.name}')
    print(f'Title: {title}')
    print('H1:', ' | '.join(h1))
    print('H2:', ' | '.join(h2[:8]))
    print('Footer:', footer_text[:260])
    print('Links:', '; '.join([f'{t}->{h}' for t,h in links[:25]]))
    if risks:
        print('Risks:')
        for pat, ctx in risks[:20]:
            print(f'- {pat}: {ctx}')
    else:
        print('Risks: none')
    print()
