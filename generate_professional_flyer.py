from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors

# Output PDF
output_pdf = "GreenLeaf_Professional_Flyer.pdf"

# Create PDF
doc = SimpleDocTemplate(output_pdf, pagesize=letter, leftMargin=0.5*inch, rightMargin=0.5*inch, topMargin=0.5*inch, bottomMargin=0.5*inch)
styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle('Title', parent=styles['Title'], fontSize=36, alignment=1, spaceAfter=10, textColor=colors.HexColor('#1B5E20'), fontName='Helvetica-Bold')
subtitle_style = ParagraphStyle('Subtitle', parent=styles['Heading2'], fontSize=20, alignment=1, spaceAfter=15, textColor=colors.HexColor('#4CAF50'))
heading_style = ParagraphStyle('Heading', parent=styles['Heading1'], fontSize=16, spaceAfter=10, textColor=colors.HexColor('#1B5E20'), fontName='Helvetica-Bold')
normal_style = ParagraphStyle('Normal', parent=styles['Normal'], fontSize=11, leading=14, alignment=4)
highlight_style = ParagraphStyle('Highlight', parent=styles['Normal'], fontSize=12, leading=15, textColor=colors.HexColor('#2E7D32'), fontName='Helvetica-Bold')
contact_style = ParagraphStyle('Contact', parent=styles['Normal'], fontSize=12, leading=16, alignment=1, textColor=colors.HexColor('#1B5E20'), fontName='Helvetica-Bold')
bullet_style = ParagraphStyle('Bullet', parent=styles['Normal'], leftIndent=25, bulletIndent=15, fontSize=11, leading=13)

# Build story
story = []

# Page 1 Header
story.append(Paragraph("GREENLEAF INGREDIENTS", title_style))
story.append(Paragraph("Premium Botanical Extracts Supplier", subtitle_style))
story.append(Spacer(1, 0.3*inch))

# About Section
story.append(Paragraph("About Us", heading_style))
story.append(Paragraph(
    "GreenLeaf Ingredients is a Perth-based supplier of premium botanical extracts serving cosmetic, personal care, and nutraceutical manufacturers across Australia. We specialise in helping small and medium manufacturers access bulk botanical ingredients without the large minimum order quantities normally required by global suppliers.",
    normal_style
))
story.append(Spacer(1, 0.3*inch))

# Why Choose Us
story.append(Paragraph("Why Choose GreenLeaf Ingredients?", heading_style))
reasons = [
    "Direct sourcing from established global manufacturers",
    "Flexible quantities tailored to your formulation needs",
    "Reliable international supply coordination",
    "Competitive wholesale pricing for B2B partners",
    "Professional ingredient sourcing expertise"
]
for reason in reasons:
    story.append(Paragraph(f"• {reason}", bullet_style))

story.append(PageBreak())

# Page 2
story.append(Paragraph("Our Product Range", heading_style))
story.append(Spacer(1, 0.2*inch))

# Product Categories
categories = [
    ("Mushroom Extracts", "Lion's Mane, Shiitake, Maitake, Chaga, Reishi - 50% Polysaccharides"),
    ("Berry Extracts", "Acai, Blueberry, Cranberry, Blackberry - 10:1 concentrates"),
    ("Adaptogenic Herbs", "Ashwagandha, Giloy, Neem, Gokhru, Shilajit - Standardized extracts"),
    ("Specialized Extracts", "Turmeric (95% Curcuminoids), Milk Thistle (80% Silymarin), Garcinia (60% HCA)"),
    ("Ginseng Varieties", "Red Korean, Panax, Siberian - with standardized Ginsenosides"),
    ("Plant Powders", "Spirulina (65% Protein), Maca (10:1), Seabuckthorn (10:1)"),
    ("Premium Range", "Aloe Vera, Acai, Cordyceps, Shilajit, and 35+ more extracts available")
]

product_table_data = [["Product Category", "Specifications"]]
for cat, spec in categories:
    product_table_data.append([Paragraph(cat, highlight_style), Paragraph(spec, normal_style)])

product_table = Table(product_table_data, colWidths=[2.2*inch, 3.8*inch])
product_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4CAF50')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 12),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#E8F5E9')),
    ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#4CAF50')),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#E8F5E9'), colors.HexColor('#F1F8E9')]),
]))
story.append(product_table)
story.append(Spacer(1, 0.4*inch))

# Applications
story.append(Paragraph("Ideal Applications", heading_style))
apps = ["Skincare Products", "Haircare Formulations", "Personal Care", "Natural Cosmetics", "Nutraceutical Supplements"]
app_text = " • ".join(apps)
story.append(Paragraph(app_text, normal_style))
story.append(Spacer(1, 0.4*inch))

# Contact
story.append(Paragraph("Get in Touch", heading_style))
story.append(Spacer(1, 0.2*inch))
contact_info = """
<b>Website:</b> www.greenleafingredients.com.au<br/>
<b>Email:</b> info@greenleafingredients.com.au<br/>
<b>Phone:</b> +61 448 467 962<br/>
<b>Location:</b> Perth, Western Australia
"""
story.append(Paragraph(contact_info, contact_style))
story.append(Spacer(1, 0.3*inch))

# Call to Action
cta = "Partner with GreenLeaf Ingredients for reliable, high-quality botanical extract sourcing."
story.append(Paragraph(cta, ParagraphStyle('CTA', parent=styles['Normal'], fontSize=13, alignment=1, textColor=colors.HexColor('#1B5E20'), fontName='Helvetica-Bold', leading=16)))

# Build PDF
doc.build(story)

print(f"Professional flyer created: {output_pdf}")