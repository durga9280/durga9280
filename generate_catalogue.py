from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.pdfgen import canvas

# Template image
template_image = "ChatGPT Image Mar 6, 2026, 12_03_21 AM.png"

# Output PDF
output_pdf = "GreenLeaf_Catalogue_2026.pdf"

# Content
title = "GREENLEAF INGREDIENTS Botanical Extracts Catalogue 2026"
contact = """Website: www.greenleafingredients.com.au
Email: info@greenleafingredients.com.au
Phone: +61 448 467 962
Location: Perth, Western Australia"""

about = """ABOUT GREENLEAF INGREDIENTS
Trusted Supplier of Botanical Extracts for Cosmetic, Personal Care & Nutraceutical Manufacturers

GreenLeaf Ingredients is a Perth-based supplier of botanical extracts serving cosmetic, personal care and nutraceutical manufacturers across Australia.

Our focus is sourcing high-quality plant-based ingredients from reliable global producers and supplying them according to buyer-specific requirements.

We specialise in helping small and medium manufacturers access bulk botanical ingredients without the large minimum order quantities normally required by global suppliers."""

approach = """Our Approach
• Direct sourcing from established manufacturers
• Requirement-based supply for formulation needs
• Flexible quantities for smaller manufacturers
• Reliable international supply coordination
• Professional B2B ingredient sourcing service"""

applications = """Applications
• Skincare products
• Haircare formulations
• Personal care products
• Natural cosmetic formulations
• Herbal wellness products"""

header = """BOTANICAL ACTIVE INGREDIENTS
Premium Quality Extracts for Cosmetic & Nutraceutical Applications"""

products = [
    ("1", "Aloe Vera Extract Powder", "200:1"),
    ("2", "Aloe Vera Extract Powder", "100:1"),
    ("3", "Lion's Mane Extract", "50% Polysaccharide, 10% Beta-glucan"),
    ("4", "Shiitake Extract", "50% Polysaccharide, 10% Beta-glucan"),
    ("5", "Maitake Extract", "50% Polysaccharide, 10% Beta-glucan"),
    ("6", "Chaga Extract", "50% Polysaccharide, 10% Beta-glucan"),
    ("7", "Reishi Extract", "50% Polysaccharide, 10% Beta-glucan"),
    ("8", "Cordyceps Extract", "50% Polysaccharide, 10% Beta-glucan"),
    ("9", "Acai Berry Extract", "10:1"),
    ("10", "Blueberry Extract", "10:1"),
    ("11", "Cranberry Extract", "10:1"),
    ("12", "Blackberry Extract", "10:1"),
    ("13", "Ashwagandha Extract", "5% Withanolides"),
    ("14", "Giloy Extract", "5% Bitter"),
    ("15", "Neem Extract", "5% Bitter"),
    ("16", "Gokhru Extract", "40% Saponins"),
    ("17", "Shilajit Extract", "20% Fulvic Acid"),
    ("18", "Garcinia Extract", "60% HCA"),
    ("19", "Milk Thistle Extract", "80% Silymarin"),
    ("20", "Turmeric Extract", "95% Curcuminoids"),
    ("21", "Stevia Extract", "97% Reb A"),
    ("22", "Apple Cider Vinegar Powder", "10% Acidity"),
    ("23", "D-Alpha Tocopheryl Succinate", "1210 IU/gm"),
    ("24", "Tongkat Ali Extract", "100:1 / 1% Eurycomanone"),
    ("25", "Valerian Root Extract", "0.8% Valeric Acid"),
    ("26", "Shatavari Extract", "40% Saponins"),
    ("27", "Seabuckthorn Extract", "10:1"),
    ("28", "Triphala Extract", "3:1"),
    ("29", "Red Korean Ginseng Extract", "10% Ginsenoside"),
    ("30", "Panax Ginseng Extract", "10% Ginsenoside"),
    ("31", "Siberian Ginseng Extract", "3.5% Eleutheroside"),
    ("32", "Spirulina Powder", "65% Protein"),
    ("33", "Black Maca Extract", "10:1 / 0.6% Macamides"),
    ("34", "Yellow Maca Extract", "10:1"),
    ("35", "Horny Goat Weed Extract", "10% Icariin"),
    ("36", "Ajuga Extract", "10% Turkesterone"),
    ("37", "Cyanotis Arachnoidea Extract", "20% Ecdysterone"),
    ("38", "Tribulus Extract", "80% / 20%"),
    ("39", "Epicatechin Extract", "98%"),
    ("40", "Cistanche Extract", "25%"),
    ("41", "Sophora Japonica Extract", "Quercetin 98%"),
    ("42", "Bromelain Extract", "2400 GDU"),
    ("43", "Grape Seed Extract", "95% Proanthocyanidins"),
]

closing = """THANK YOU

Partner with GreenLeaf Ingredients
Premium botanical extracts for cosmetic, personal care & nutraceutical manufacturers.

GreenLeaf Ingredients is committed to supplying high-quality botanical extracts sourced from trusted global producers.

We support small and medium manufacturers with flexible quantities and reliable sourcing solutions tailored to their formulation needs.

Website: www.greenleafingredients.com.au
Email: info@greenleafingredients.com.au
Phone: +61 448 467 962
Location: Perth, Western Australia"""

# Function to draw background
def draw_background(canvas, doc):
    canvas.drawImage(template_image, 0, 0, width=letter[0], height=letter[1])

# Create PDF
doc = SimpleDocTemplate(output_pdf, pagesize=letter)
styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle('Title', parent=styles['Title'], fontSize=24, alignment=1, spaceAfter=20)
heading_style = ParagraphStyle('Heading', parent=styles['Heading1'], fontSize=18, spaceAfter=15)
normal_style = styles['Normal']
bullet_style = ParagraphStyle('Bullet', parent=styles['Normal'], leftIndent=20, bulletIndent=10)

# Build story
story = []

# Title page
story.append(Paragraph(title, title_style))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph(contact, normal_style))
story.append(PageBreak())

# About
story.append(Paragraph("ABOUT GREENLEAF INGREDIENTS", heading_style))
story.append(Paragraph(about, normal_style))
story.append(Spacer(1, 0.5*inch))

# Approach
story.append(Paragraph("Our Approach", heading_style))
for line in approach.split('\n')[1:]:  # Skip header
    if line.strip():
        story.append(Paragraph(line, bullet_style))
story.append(Spacer(1, 0.5*inch))

# Applications
story.append(Paragraph("Applications", heading_style))
for line in applications.split('\n')[1:]:
    if line.strip():
        story.append(Paragraph(line, bullet_style))
story.append(PageBreak())

# Products
story.append(Paragraph(header, heading_style))
story.append(Spacer(1, 0.5*inch))

# Table
table_data = [['No.', 'Product', 'Specification']] + products
table = Table(table_data)
table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.grey),
    ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,0), 12),
    ('BOTTOMPADDING', (0,0), (-1,0), 12),
    ('BACKGROUND', (0,1), (-1,-1), colors.beige),
    ('GRID', (0,0), (-1,-1), 1, colors.black),
]))
story.append(table)
story.append(PageBreak())

# Closing
story.append(Paragraph(closing, normal_style))

# Build PDF with background
doc.build(story, onFirstPage=draw_background, onLaterPages=draw_background)

print(f"Catalogue created: {output_pdf}")