from pypdf import PdfReader, PdfWriter

# Input PDF
input_pdf = "Green Leaf ingredients 2026 catalogue.pdf"
output_pdf = "Green Leaf ingredients 2026 catalogue_even.pdf"

# Standard page size: A4 in points (1/72 inch)
standard_width = 595
standard_height = 842

# Open the input PDF
reader = PdfReader(input_pdf)
writer = PdfWriter()

for page in reader.pages:
    # Get current page size
    mediabox = page.mediabox
    current_width = float(mediabox.width)
    current_height = float(mediabox.height)
    
    # Calculate scale to fit into A4, maintaining aspect ratio
    scale_x = standard_width / current_width
    scale_y = standard_height / current_height
    scale = min(scale_x, scale_y)
    
    # Scale the page
    page.scale(scale, scale)
    
    # Add to writer
    writer.add_page(page)

# Save the new PDF
with open(output_pdf, "wb") as f:
    writer.write(f)

print(f"Processed PDF saved as {output_pdf}")