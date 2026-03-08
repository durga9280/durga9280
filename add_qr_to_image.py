from PIL import Image
import qrcode

# Paths
input_image = "ChatGPT Image Mar 6, 2026, 12_03_21 AM.png"
output_image = "ChatGPT Image Mar 6, 2026, 12_03_21 AM_with_qr.png"

# Generate QR code
url = "https://www.greenleafingredients.com.au"
qr_img = qrcode.make(url)

# Resize qr code to appropriate size (e.g., 300x300 pixels)
qr_size = 300
qr_img = qr_img.resize((qr_size, qr_size))

# Open original image
base = Image.open(input_image).convert("RGBA")

# Position QR code at bottom right with some margin
overlay = Image.new("RGBA", base.size)

margin = 50
x = base.width - qr_size - margin
y = base.height - qr_size - margin

overlay.paste(qr_img, (x, y))

# Composite and save
combined = Image.alpha_composite(base, overlay)
combined.convert("RGB").save(output_image)

print(f"Saved new image with QR code: {output_image}")