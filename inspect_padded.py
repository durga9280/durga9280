from pypdf import PdfReader
reader = PdfReader("Green Leaf ingredients 2026 catalogue_padded.pdf")
for i,page in enumerate(reader.pages, start=1):
    print(f"Page {i}: {float(page.mediabox.width)}x{float(page.mediabox.height)}")
