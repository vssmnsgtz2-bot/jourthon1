from pathlib import Path

root = Path('/home/ubuntu/jourthon_static_site')
replacements = {
    "Rooted in North America. Built for Global Brands.": "Rooted in North America. Built for Supplement Brands and Private-Label Clients.",
    "A focused journey in health supplement launch support": "A focused journey in health supplement manufacturing support",
    "Tell us what you want to launch.": "Tell us what you want to manufacture.",
    "The partner that understands <em>science, compliance, and market entry</em>": "The partner that understands <em>science, compliance, and production execution</em>",
    "Most service providers focus on one step. Jourthon connects the whole launch chain so founders, distributors, and international brands can move with greater clarity.": "Most service providers focus on one step. Jourthon connects formulation, documentation, manufacturing, packaging, and supply coordination so founders, distributors, and international brands can move with greater clarity.",
    "Global Client Service": "Global Manufacturing Support",
    "Jourthon bridges international brand teams with North American supplier networks, documentation expectations, and launch timelines.": "Jourthon bridges international brand teams with North American supplier networks, documentation expectations, production planning, and reorder timelines.",
    "First SKU launch": "First SKU manufacturing plan",
    "A founder has a category idea but needs formula direction, packaging guidance, compliance review, manufacturing, and launch coordination.": "A founder has a category idea but needs formula direction, packaging guidance, compliance review, contract manufacturing, and production coordination.",
    "Canada or US entry": "Canada or US production readiness",
    "An overseas wellness brand wants to adapt an existing product for North American requirements and establish local supply support.": "An overseas supplement brand wants to adapt an existing formula for North American requirements and establish reliable production and supply support.",
    "Market readiness": "Production readiness",
    "market readiness": "production readiness",
    "Market-Ready": "Production-Ready",
    "market-ready": "production-ready",
    "market entry": "production and supply readiness",
    "Market entry": "Production and supply readiness",
    "launch stage": "production stage",
    "launch coordination": "production coordination",
    "launch timelines": "production timelines",
    "launch support": "manufacturing support",
    "Global Brands": "Supplement Brands and Private-Label Clients",
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

print('Second-pass factory language refinement complete.')
