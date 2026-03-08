from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.pdfgen import canvas

# Template image
template_image = "ChatGPT Image Mar 6, 2026, 12_03_21 AM.png"

# Output PDF
output_pdf = "GreenLeaf_Flyer_2026.pdf"

# Content for flyer
title = "GREENLEAF INGREDIENTS"
subtitle = "Premium Botanical Extracts for Your Formulations"

about = """Trusted Supplier of Botanical Extracts for Cosmetic, Personal Care & Nutraceutical Manufacturers.

We source high-quality plant-based ingredients from reliable global producers and supply them according to your specific requirements."""

approach = """Our Approach:
• Direct sourcing from established manufacturers
• Flexible quantities for small and medium manufacturers
• Reliable international supply coordination
• Professional B2B ingredient sourcing service"""

products_highlight = """Featured Botanical Extracts:
- Aloe Vera Extract Powder (200:1 & 100:1)
- Mushroom Extracts (Lion's Mane, Shiitake, Maitake, Chaga, Reishi) - 50% Polysaccharides
- Berry Extracts (Acai, Blueberry, Cranberry, Blackberry) - 10:1
- Adaptogens (Ashwagandha, Giloy, Neem, Gokhru, Shilajit)
- And 35+ more premium extracts...

Perfect for Skincare, Haircare, Personal Care & Nutraceuticals."""

contact = """Partner with Us Today!
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
title_style = ParagraphStyle('Title', parent=styles['Title'], fontSize=28, alignment=1, spaceAfter=10, textColor=colors.darkgreen)
subtitle_style = ParagraphStyle('Subtitle', parent=styles['Heading2'], fontSize=18, alignment=1, spaceAfter=20)
normal_style = ParagraphStyle('Normal', parent=styles['Normal'], fontSize=12, leading=14)
bullet_style = ParagraphStyle('Bullet', parent=styles['Normal'], leftIndent=20, bulletIndent=10, fontSize=12, leading=14)
highlight_style = ParagraphStyle('Highlight', parent=styles['Normal'], fontSize=14, leading=16, textColor=colors.darkblue)

# Build story
story = []

# Page 1
story.append(Paragraph(title, title_style))
story.append(Paragraph(subtitle, subtitle_style))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph(about, normal_style))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph(approach, bullet_style))
story.append(PageBreak())

# Page 2
story.append(Paragraph("Our Product Range", styles['Heading1']))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph(products_highlight, highlight_style))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph(contact, normal_style))

# Build PDF with background
doc.build(story, onFirstPage=draw_background, onLaterPages=draw_background)

print(f"Flyer created: {output_pdf}")