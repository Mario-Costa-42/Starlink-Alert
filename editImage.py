from PIL import Image, ImageDraw, ImageFont
import os
print(os.path.exists("/home/m4ri0/Let's-Code-Again/playing-with-python/Scraping-data-with-python/assets/spacecoolimage.jpg")) 

# Open an image
image = Image.open("/home/m4ri0/Let's-Code-Again/playing-with-python/Scraping-data-with-python/assets/spacecoolimage.jpg")

# Create an ImageDraw object
draw = ImageDraw.Draw(image)

# Choose a font and size (you may need to provide the full path to the font)
# You can download or use a system font, for example, "arial.ttf"
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)

# Define the text and position
text = "Hello, World!"
position = (50, 50)  # (x, y) coordinates where the text will appear

# Define text color (R, G, B)
text_color = (255, 255, 255)  # White color

# Add text to the image
draw.text(position, text, font=font, fill=text_color)

# Save the edited image
image.save("image_with_text.jpg")


