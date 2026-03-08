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

# Position QR code at right side, moved upward to avoid hiding text
margin_bottom = 250
margin_right = 50

# Position at bottom right
x = base.width - qr_size - margin_right
y = base.height - qr_size - margin_bottom

# Paste QR code
base.paste(qr_img, (x, y))

# Add text above the QR code
draw = ImageDraw.Draw(base)
text = "Scan to explore our catalogue"

# Try to use bold/thick font to match flyer style
font_size = 18
try:
    # Try bold Arial first
    font = ImageFont.truetype("arialbd.ttf", font_size)
except:
    try:
        # Try regular Arial with larger size
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        try:
            # Try Calibri Bold
            font = ImageFont.truetype("calibrib.ttf", font_size)
        except:
            font = ImageFont.load_default()

# Calculate text position (above QR code on the right)
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

# Position text above the QR code, right-aligned with QR
text_x = x + (qr_size - text_width) // 2
text_y = y - text_height - 10

# Draw text in dark color with semi-bold appearance
draw.text((text_x, text_y), text, fill=(0, 0, 0), font=font)

# Save the image
base.save(output_image)

print(f"Saved new image with QR code and text: {output_image}")