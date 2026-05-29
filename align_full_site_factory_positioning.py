from pathlib import Path

root = Path('/home/ubuntu/jourthon_static_site')
pages = list(root.glob('*.html'))

replacements = {
    "North America Supplement Launch Partner": "North America Supplement Contract Manufacturing Partner",
    "Jourthon Nutrition — North America Supplement Launch Partner": "Jourthon Nutrition — Supplement Contract Manufacturing Partner",
    "North America's full-chain health supplement launch partner. From formula to shelf, Jourthon helps global wellness brands build compliant, market-ready products.": "North America's full-chain supplement manufacturing and private-label partner. From formulation to finished goods, Jourthon helps brands coordinate compliant, market-ready production.",
    "Launch Your Supplement Brand in North America — <em>From Formula to Shelf.</em>": "Build Your Supplement Product Line in North America — <em>From Formula to Finished Goods.</em>",
    "Jourthon Nutrition Inc. helps global wellness brands develop compliant, market-ready supplements through integrated formulation, regulatory, manufacturing, packaging, supply chain, and launch support.": "Jourthon Nutrition Inc. helps supplement brands, distributors, and private-label clients develop and manufacture compliant, market-ready products through integrated formulation, regulatory, manufacturing, packaging, and supply chain coordination.",
    "Start Your Launch Plan": "Start Your Manufacturing Plan",
    "Your Launch Journey": "Your Manufacturing Journey",
    "A clearer path from <em>idea to shelf</em>": "A clearer path from <em>concept to finished goods</em>",
    "Jourthon turns a complex supplement launch into a managed sequence of decisions, documents, partners, and production milestones.": "Jourthon turns supplement product development into a managed sequence of formulation decisions, documentation, manufacturing coordination, packaging, and production milestones.",
    "Manufacture & Launch": "Manufacture & Deliver",
    "Through qualified manufacturing, packaging, warehousing, and logistics partners, we help move your product toward market entry.": "Through qualified production, packaging, warehousing, and logistics resources, we help move your product toward finished-goods readiness and market supply.",
    "Integrated Launch Support": "Integrated Manufacturing Support",
    "One accountable partner coordinating formulation, compliance, manufacturing, packaging, and supply chain execution.": "One accountable partner coordinating formulation, compliance, contract manufacturing, packaging, and supply chain execution.",
    "Solutions for Every Stage": "Manufacturing Solutions for Every Stage",
    "Choose the path that matches <em>your launch goal</em>": "Choose the path that matches <em>your production goal</em>",
    "Rather than presenting services as separate tasks, Jourthon organizes them around the real situations supplement brands face.": "Rather than presenting services as isolated tasks, Jourthon organizes them around the real manufacturing and private-label situations supplement brands face.",
    "New Brand Launch": "Product Line Development",
    "Build a market-ready product from zero": "Develop a manufacturable supplement product line",
    "For founders and wellness companies developing a first supplement SKU or full product line for North America.": "For founders, distributors, and brand owners developing a first supplement SKU or a complete private-label product line for North America.",
    "Explore launch support": "Explore development support",
    "Compliance Fast Track": "Regulatory Readiness",
    "Prepare existing products for market entry": "Prepare formulas and labels for production",
    "For brands that already have a formula and need documentation, label review, and regulatory pathway support.": "For clients that already have a formula and need documentation, label review, claims screening, and production-readiness support.",
    "Check compliance needs": "Check regulatory needs",
    "Private Label & Scale": "Private Label Manufacturing",
    "Manufacture, package, and scale efficiently": "Manufacture, package, and reorder efficiently",
    "For distributors, retailers, and established brands seeking qualified production and supply chain management.": "For distributors, retailers, and established brands seeking qualified contract manufacturing, packaging, MOQ planning, and ongoing supply coordination.",
    "services.html#launch": "services.html#contract-manufacturing",
    "services.html#compliance": "services.html#regulatory-compliance",
    "services.html#manufacturing": "services.html#nutritional-supplements",
    "services.html#market": "services.html#packaging",
    "Your next supplement brand starts here.": "Your next supplement product line starts with manufacturing clarity.",
    "Submit your product brief and Jourthon will help identify the right pathway across formulation, compliance, manufacturing, packaging, and launch support.": "Submit your product brief and Jourthon will help identify the right pathway across formulation, compliance, contract manufacturing, packaging, and supply coordination.",
    "Rooted in North America. Built for Global Brands.": "Rooted in North America. Built for Global Supplement Brands.",
    "A full-chain partner for supplement companies": "A full-chain manufacturing partner for supplement companies",
    "A focused journey in health supplement launch support": "A focused journey in health supplement manufacturing support",
    "Partner with Jourthon to build your next product.": "Partner with Jourthon to manufacture your next product.",
    "Tell us what you want to launch.": "Tell us what you want to manufacture.",
    "Start with a clear product brief": "Start with a clear manufacturing brief",
    "Inquiry Type New Brand Launch Compliance Check Private Label Manufacturing Packaging & Labelling Market Entry Support": "Inquiry Type Product Line Development Regulatory Readiness Private Label Manufacturing Packaging & Labelling Supply Chain / Market Entry",
    "Need a compliance review before launch?": "Need a compliance review before production?",
    "Request Compliance Check": "Request Regulatory Review",
    "Ready to build your product?": "Ready to manufacture your product?",
    "Share your product category, dosage form, target market, and launch stage. Jourthon will help identify the right service path.": "Share your product category, dosage form, target market, and production stage. Jourthon will help identify the right manufacturing and service path.",
    "From scientific formulation and regulatory compliance to contract manufacturing, packaging, design, and market entry — Jourthon supports every step of the supplement lifecycle while preserving the original service content.": "From scientific formulation and regulatory compliance to contract manufacturing, packaging, design, and supply coordination — Jourthon supports every step of the supplement production lifecycle.",
    "Health Canada. FDA. Global market entry — coordinated with a compliance-first mindset.": "Health Canada. FDA-oriented review. Export readiness — coordinated with a compliance-first mindset.",
    "DIN Drug Identification Number registration support": "DIN registration support, where applicable",
    "Product license applications and renewals coordination": "Product licence applications and renewals coordination",
    "Adverse reaction reporting and post-market surveillance process support": "Post-market documentation and reporting process support",
    "Market Entry Support": "Supply Chain Support",
    "Submit Your Product Brief": "Submit Manufacturing Brief",
    "Submit Product Brief": "Submit Manufacturing Brief",
    "Project Inquiry": "Manufacturing Inquiry",
}

for p in pages:
    text = p.read_text(encoding='utf-8')
    for old, new in replacements.items():
        text = text.replace(old, new)
    p.write_text(text, encoding='utf-8')

# Mirror to deploy package if exists
package = Path('/home/ubuntu/jourthon_deploy_package')
if package.exists():
    for p in pages:
        target = package / p.name
        if target.exists():
            target.write_text(p.read_text(encoding='utf-8'), encoding='utf-8')
    # copy style in case service styles changed earlier
    for asset in ['style.css', 'script.js']:
        if (root/asset).exists() and (package/asset).exists():
            (package/asset).write_text((root/asset).read_text(encoding='utf-8'), encoding='utf-8')

print('Aligned all pages to supplement contract manufacturing positioning.')
