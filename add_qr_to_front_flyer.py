from PIL import Image
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

# Position QR code at bottom left with margin
margin = 40
x = margin
y = height - qr_size - margin

print(f"Placing QR code at bottom left: x={x}, y={y}")

# Paste QR code
base.paste(qr_img, (x, y))

# Save the image
base.save(output_image)

print(f"Saved new image with QR code: {output_image}")