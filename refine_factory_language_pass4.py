from pathlib import Path
root = Path('/home/ubuntu/jourthon_static_site')
replacements = {
    'Tell us what you want to <em>launch.</em>': 'Tell us what you want to <em>manufacture.</em>',
    'New supplement launches, compliance checks, manufacturing quotes, packaging coordination, and North American production and supply readiness planning.': 'New supplement product lines, compliance checks, manufacturing quotes, packaging coordination, and North American production and supply readiness planning.',
    'compliant, production-ready production.': 'compliant, production-ready finished goods.',
}
for p in root.glob('*.html'):
    text = p.read_text(encoding='utf-8')
    for old, new in replacements.items():
        text = text.replace(old, new)
    p.write_text(text, encoding='utf-8')

package = Path('/home/ubuntu/jourthon_deploy_package')
if package.exists():
    for p in root.glob('*.html'):
        target = package / p.name
        if target.exists():
            target.write_text(p.read_text(encoding='utf-8'), encoding='utf-8')
print('Fourth-pass cleanup complete.')
