from PIL import Image, ImageDraw, ImageFont
import os
import random

print(os.path.exists("images")) 
# Caminho para a pasta onde estão as imagens
caminho_da_pasta = 'images'

# Lista todos os arquivos da pasta
arquivos = os.listdir(caminho_da_pasta)

# Filtra apenas as imagens que começam com "spaceimage"
imagens = [arquivo for arquivo in arquivos if arquivo.startswith('spaceimage')]

# Seleciona uma imagem aleatoriamente
imagem_aleatoria = random.choice(imagens)

# Exibe o nome da imagem selecionada
print(f'A imagem selecionada aleatoriamente é: {imagem_aleatoria}')

# Open an image
image = Image.open(f'images/{imagem_aleatoria}')

# Create an ImageDraw object
draw = ImageDraw.Draw(image)

# Choose a font and size (you may need to provide the full path to the font)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)

# Define the first text and position
text1 = "starlink estará visivel no céu \n as [00:00] do dia [00/00/0000]"
position1 = (30, 50)  # (x, y) coordinates where the text will appear

# Define the second text and position
text2 = "O evento durará x minutos \n nas coordenadas: \n xx graus [direção cardeal]\n xx graus [direção cardeal] \n xx graus [direção cardeal]"
position2 = (30, 250)  # (x, y) coordinates where the text will appear

# Define text color (R, G, B)
text_color = (255, 255, 255)  # White color

# Add text to the image
draw.text(position1, text1, font=font, fill=text_color)
draw.text(position2, text2, font=font, fill=text_color)

# Save the edited image
image.save("createdImages/image_with_text.jpg")


