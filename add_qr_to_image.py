from PIL import Image
import qrcode

# Paths
input_image = "Greenleaf ingredient flyer - A4 size.png"
output_image = "Greenleaf ingredient flyer - A4 size_with_qr.png"

# Generate QR code
url = "https://www.greenleafingredients.com.au"
qr_img = qrcode.make(url)

# Resize qr code to appropriate size (e.g., 300x300 pixels)
qr_size = 300
qr_img = qr_img.resize((qr_size, qr_size))

# Open original image
base = Image.open(input_image).convert("RGBA")

# Position QR code at top right with some margin
overlay = Image.new("RGBA", base.size)

margin = 50
x = base.width - qr_size - margin
y = margin

overlay.paste(qr_img, (x, y))

# Composite and save
combined = Image.alpha_composite(base, overlay)
combined.convert("RGB").save(output_image)

print(f"Saved new image with QR code: {output_image}")