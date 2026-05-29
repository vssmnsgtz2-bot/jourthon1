from pathlib import Path
root = Path('/home/ubuntu/jourthon_static_site')
replacements = {
    'Successful supplement launches require formula decisions, packaging choices, regulatory documentation, supplier coordination, quality control,': 'Successful supplement manufacturing programs require formula decisions, packaging choices, regulatory documentation, supplier coordination, quality control,',
    '<span>Launch stages</span>': '<span>Project stages</span>',
    'We translate a complex launch into practical steps, accountable deliverables, and realistic timelines.': 'We translate a complex manufacturing project into practical steps, accountable deliverables, and realistic timelines.',
    'Jourthon continues helping international brands clarify Canadian and US launch pathways.': 'Jourthon continues helping international brands clarify Canadian and US production and supply pathways.',
    'practical launch planning, supplier coordination, and production-ready execution.': 'practical production planning, supplier coordination, and production-ready execution.',
    'Tell us where you are in the launch journey, and we will help you identify the next step.': 'Tell us where you are in the manufacturing project, and we will help you identify the next step.',
    'launch-ready compliance files': 'production-ready compliance files',
    'Supplement formulation and launch planning': 'Supplement formulation and manufacturing planning',
    'New brand launch': 'New supplement product line',
    'Launch roadmap and supplier matching': 'Production roadmap and supplier matching',
    '<h3>Launch Documentation</h3>': '<h3>Production Documentation</h3>',
    'Launch Documentation': 'Production Documentation',
    'product documentation, Health Canada or FDA-related requirements, and launch-ready compliance files.': 'product documentation, Health Canada or FDA-related requirements, and production-ready compliance files.',
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
print('Fifth-pass launch-to-manufacturing refinement complete.')
