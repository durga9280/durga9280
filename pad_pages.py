from pypdf import PdfReader, PdfWriter

input_pdf = "Green Leaf ingredients 2026 catalogue.pdf"
output_pdf = "Green Leaf ingredients 2026 catalogue_padded.pdf"

standard_width = 595
standard_height = 842

reader = PdfReader(input_pdf)
writer = PdfWriter()

for page in reader.pages:
    # create a blank page at standard size
    new_page = writer.add_blank_page(width=standard_width, height=standard_height)
    
    # get current size
    w = float(page.mediabox.width)
    h = float(page.mediabox.height)
    
    # calculate offsets to center original page
    x_offset = (standard_width - w) / 2
    y_offset = (standard_height - h) / 2
    
    # merge the page onto new_page with translation
    new_page.merge_translated_page(page, tx=x_offset, ty=y_offset)
    
# save
with open(output_pdf, "wb") as f:
    writer.write(f)

print(f"Created padded PDF: {output_pdf}")
