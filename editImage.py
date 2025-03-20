from PIL import Image, ImageDraw, ImageFont
import os
import sys
import random
import subprocess

# Path to the folder containing images
caminho_da_pasta = 'images'

# List all files in the folder
arquivos = os.listdir(caminho_da_pasta)

# Filter images that start with "spaceimage"
imagens = [arquivo for arquivo in arquivos if arquivo.startswith('spaceimage')]

# Select a random image
imagem_aleatoria = random.choice(imagens)


# Open the selected image
image = Image.open(f'images/{imagem_aleatoria}')

# Create an ImageDraw object
draw = ImageDraw.Draw(image)

# Choose a bold font
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font_size = 36
font = ImageFont.truetype(font_path, font_size)

# Define the text content
text1 = f"Starlink estará visível no céu\nàs {sys.argv[1]}\nno dia {sys.argv[2]}"
position1 = (30, 50)

text2 = f"O evento durará {sys.argv[3]} minutos \nOlhe de {sys.argv[4]} \npara {sys.argv[5]}"
position2 = (30, 250)

# Colors
shadow_color = (0, 0, 0)        # Black shadow
outline_color = (0, 0, 0)     # Black outline
text_color = (255, 255, 255)    # White text

# Function to draw outlined text
def draw_text_with_outline(draw, position, text, font, text_color, outline_color, shadow_color):
    x, y = position
    
    # Draw shadow
    draw.text((x + 3, y + 3), text, font=font, fill=shadow_color)
    
    # Draw outline by drawing text multiple times slightly offset
    for dx in [-2, 0, 2]:
        for dy in [-2, 0, 2]:
            draw.text((x + dx, y + dy), text, font=font, fill=outline_color)
    
    # Draw main text
    draw.text(position, text, font=font, fill=text_color)

# Apply styled text to the image
draw_text_with_outline(draw, position1, text1, font, text_color, outline_color, shadow_color)
draw_text_with_outline(draw, position2, text2, font, text_color, outline_color, shadow_color)

# Ensure the output directory exists
output_folder = "createdImages"
os.makedirs(output_folder, exist_ok=True)

# Save the edited image
image.save("createdImages/image_with_text.jpg")

EventDateAndTime = sys.argv[6]
subprocess.run(["python3", "postOnInsta.py", EventDateAndTime])

