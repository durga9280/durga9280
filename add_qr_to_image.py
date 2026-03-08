from PIL import Image, ImageDraw, ImageFont
import qrcode

# Paths
input_image = "Greenleaf ingredient flyer - A4 size.png"
output_image = "Greenleaf ingredient flyer - A4 size_with_qr.png"

# Generate QR code
url = "https://www.greenleafingredients.com.au"
qr_img = qrcode.make(url)

# Resize qr code to appropriate size (e.g., 200x200 pixels)
qr_size = 200
qr_img = qr_img.resize((qr_size, qr_size))

# Open original image
base = Image.open(input_image).convert("RGB")

# Position QR code at bottom center with some margin
margin_bottom = 80
margin_x = 50

# Center horizontally, position at bottom
x = (base.width - qr_size) // 2
y = base.height - qr_size - margin_bottom

# Paste QR code
base.paste(qr_img, (x, y))

# Add text below the QR code
draw = ImageDraw.Draw(base)
text = "Scan to explore our catalogue"

# Try to use a nice font, fallback to default if not available
try:
    font = ImageFont.truetype("arial.ttf", 20)
except:
    font = ImageFont.load_default()

# Calculate text position (centered below QR code)
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_x = (base.width - text_width) // 2
text_y = y + qr_size + 15

# Draw text in dark color
draw.text((text_x, text_y), text, fill=(0, 0, 0), font=font)

# Save the image
base.save(output_image)

print(f"Saved new image with QR code and text: {output_image}")