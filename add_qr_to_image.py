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
margin_bottom = 120
margin_right = 50

# Position at bottom right
x = base.width - qr_size - margin_right
y = base.height - qr_size - margin_bottom

# Paste QR code
base.paste(qr_img, (x, y))

# Add text above the QR code in 2 lines
draw = ImageDraw.Draw(base)
text_line1 = "Scan to"
text_line2 = "explore our"
text_line3 = "catalogue"

# Try to use bold/thick font to match flyer style
font_size = 36
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

# Calculate text position for multiple lines (above QR code on the right)
text_bbox1 = draw.textbbox((0, 0), text_line1, font=font)
text_width1 = text_bbox1[2] - text_bbox1[0]
text_height = text_bbox1[3] - text_bbox1[1]

# Position text above the QR code, centered with QR
line_spacing = 5
total_text_height = (text_height * 3) + (line_spacing * 2)

text_x1 = x + (qr_size - text_width1) // 2
text_y1 = y - total_text_height - 10

text_bbox2 = draw.textbbox((0, 0), text_line2, font=font)
text_width2 = text_bbox2[2] - text_bbox2[0]
text_x2 = x + (qr_size - text_width2) // 2
text_y2 = text_y1 + text_height + line_spacing

text_bbox3 = draw.textbbox((0, 0), text_line3, font=font)
text_width3 = text_bbox3[2] - text_bbox3[0]
text_x3 = x + (qr_size - text_width3) // 2
text_y3 = text_y2 + text_height + line_spacing

# Find the bounding box for all 3 lines of text to draw background
max_text_width = max(text_width1, text_width2, text_width3)
box_padding = 10
box_left = x + (qr_size - max_text_width) // 2 - box_padding
box_top = text_y1 - box_padding
box_right = box_left + max_text_width + (box_padding * 2)
box_bottom = text_y3 + text_height + box_padding

# Create a background with semi-transparent white
background_color = (255, 255, 255, 180)  # White with transparency

# Draw semi-transparent background rectangle
overlay_bg = Image.new("RGBA", base.size, (0, 0, 0, 0))
draw_bg = ImageDraw.Draw(overlay_bg)
draw_bg.rectangle([box_left, box_top, box_right, box_bottom], fill=background_color)

# Composite the background onto the base image
base = Image.alpha_composite(base.convert("RGBA"), overlay_bg).convert("RGB")

# Redraw the text on top of the background
draw = ImageDraw.Draw(base)

# Draw text in dark color with semi-bold appearance
draw.text((text_x1, text_y1), text_line1, fill=(0, 0, 0), font=font)
draw.text((text_x2, text_y2), text_line2, fill=(0, 0, 0), font=font)
draw.text((text_x3, text_y3), text_line3, fill=(0, 0, 0), font=font)

# Save the image
base.save(output_image)

print(f"Saved new image with QR code and text: {output_image}")