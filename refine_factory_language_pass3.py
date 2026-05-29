from pathlib import Path

root = Path('/home/ubuntu/jourthon_static_site')
replacements = {
    'Jourthon Nutrition Inc. — North America supplement launch partner.': 'Jourthon Nutrition Inc. — North America supplement contract manufacturing and private-label partner.',
    'The original Services page included a broad product-category section. It is now restored as a dedicated portfolio block so visitors can quickly see the types of products Jourthon can help develop, manufacture, package, and launch.': 'Jourthon supports a broad range of nutrition supplement categories, helping clients turn product concepts into manufacturable, packaged, and supply-ready private-label or contract-manufactured products.',
    'Every category. Every format. Every market segment.': 'Broad categories. Flexible formats. Practical manufacturing paths.',
    'develop, manufacture, package, and launch': 'develop, manufacture, package, and supply',
    'develop, manufacture, package, and production and supply readiness': 'develop, manufacture, package, and supply',
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
print('Third-pass refinement complete.')
