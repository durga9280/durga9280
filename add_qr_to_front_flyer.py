from PIL import Image, ImageDraw, ImageFont
import qrcode

# Paths
input_image = "Front side flyer.png"
output_image = "Front side flyer_with_qr.png"

# Open the image
base = Image.open(input_image).convert("RGB")
width, height = base.size
print(f"Image dimensions: {width}x{height}")

# Generate QR code
url = "https://www.greenleafingredients.com.au"
qr_img = qrcode.make(url)

# Size the QR code appropriately
qr_size = 180
qr_img = qr_img.resize((qr_size, qr_size))

# Add text above the QR code in 3 lines
draw = ImageDraw.Draw(base)
text_line1 = "Scan to"
text_line2 = "explore our"
text_line3 = "catalogue"

# Try to use bold font
font_size = 30
try:
    font = ImageFont.truetype("seguib.ttf", font_size)
except:
    try:
        font = ImageFont.truetype("arialbd.ttf", font_size)
    except:
        font = ImageFont.load_default()

# Calculate text dimensions
text_bbox1 = draw.textbbox((0, 0), text_line1, font=font)
text_height = text_bbox1[3] - text_bbox1[1]
text_bbox2 = draw.textbbox((0, 0), text_line2, font=font)
text_width2 = text_bbox2[2] - text_bbox2[0]
text_bbox3 = draw.textbbox((0, 0), text_line3, font=font)
text_width3 = text_bbox3[2] - text_bbox3[0]

# Position text and QR code in the center area
line_spacing = 5
total_text_height = (text_height * 3) + (line_spacing * 2)
box_padding = 8

# Center horizontally, position in middle of image
center_x = (width - qr_size) // 2
qr_y = (height - total_text_height - qr_size - 30) // 2 + total_text_height + 20

# Text positions (above QR)
text_y_start = qr_y - total_text_height - 15

# Draw semi-transparent background behind text
box_left = center_x
box_right = center_x + qr_size
box_top = text_y_start - box_padding
box_bottom = qr_y

background_color = (255, 255, 255, 190)
overlay_bg = Image.new("RGBA", base.size, (0, 0, 0, 0))
draw_bg = ImageDraw.Draw(overlay_bg)
draw_bg.rectangle([box_left, box_top, box_right, box_bottom], fill=background_color)

base = Image.alpha_composite(base.convert("RGBA"), overlay_bg).convert("RGB")
draw = ImageDraw.Draw(base)

# Draw text
text_bbox1 = draw.textbbox((0, 0), text_line1, font=font)
text_width1 = text_bbox1[2] - text_bbox1[0]
text_x1 = center_x + (qr_size - text_width1) // 2
text_y1 = text_y_start

text_x2 = center_x + (qr_size - text_width2) // 2
text_y2 = text_y1 + text_height + line_spacing

text_x3 = center_x + (qr_size - text_width3) // 2
text_y3 = text_y2 + text_height + line_spacing

draw.text((text_x1, text_y1), text_line1, fill=(0, 0, 0), font=font)
draw.text((text_x2, text_y2), text_line2, fill=(0, 0, 0), font=font)
draw.text((text_x3, text_y3), text_line3, fill=(0, 0, 0), font=font)

# Paste QR code below text
base.paste(qr_img, (center_x, qr_y))

# Save the image
base.save(output_image)

print(f"Added QR code and text below position")
print(f"Saved new image: {output_image}")