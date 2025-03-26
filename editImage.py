# from PIL import Image, ImageDraw, ImageFont
# import os
# import sys
# import random
# import subprocess

# # Path to the folder containing images
# caminho_da_pasta = 'images'

# # List all files in the folder
# arquivos = os.listdir(caminho_da_pasta)

# # Filter images that start with "spaceimage"
# imagens = [arquivo for arquivo in arquivos if arquivo.startswith('spaceimage')]

# # Select a random image
# imagem_aleatoria = random.choice(imagens)


# # Open the selected image
# image = Image.open(f'images/{imagem_aleatoria}')

# # Create an ImageDraw object
# draw = ImageDraw.Draw(image)

# # Choose a bold font
# font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
# font_size = 36
# font = ImageFont.truetype(font_path, font_size)

# # Define the text content
# text1 = f"Starlink estará visível no céu\nàs {sys.argv[1]}\nno dia {sys.argv[2]}"
# position1 = (30, 50)

# text2 = f"O evento durará {sys.argv[3]} minutos \nOlhe de {sys.argv[4]} \npara {sys.argv[5]}"
# position2 = (30, 250)

# # Colors
# shadow_color = (0, 0, 0)        # Black shadow
# outline_color = (0, 0, 0)     # Black outline
# text_color = (255, 255, 255)    # White text

# # Function to draw outlined text
# def draw_text_with_outline(draw, position, text, font, text_color, outline_color, shadow_color):
#     x, y = position
    
#     # Draw shadow
#     draw.text((x + 3, y + 3), text, font=font, fill=shadow_color)
    
#     # Draw outline by drawing text multiple times slightly offset
#     for dx in [-2, 0, 2]:
#         for dy in [-2, 0, 2]:
#             draw.text((x + dx, y + dy), text, font=font, fill=outline_color)
    
#     # Draw main text
#     draw.text(position, text, font=font, fill=text_color)

# # Apply styled text to the image
# draw_text_with_outline(draw, position1, text1, font, text_color, outline_color, shadow_color)
# draw_text_with_outline(draw, position2, text2, font, text_color, outline_color, shadow_color)

# # Ensure the output directory exists
# output_folder = "createdImages"
# os.makedirs(output_folder, exist_ok=True)

# # Save the edited image
# image.save("createdImages/image_with_text.jpg")

# EventDateAndTime = sys.argv[6]
# subprocess.run(["python3", "postOnInsta.py", EventDateAndTime])

################################################################################################
######################################################################################
################################################################################################
######################################################################################
################################################################################################
######################################################################################
################################################################################################
######################################################################################
################################################################################################
######################################################################################
################################################################################################
######################################################################################

# from PIL import Image, ImageDraw, ImageFont
# import os
# import sys
# import random
# import hashlib
# import json
# import subprocess

# print("Raw JSON input:", sys.argv[1])  # Depuração

# try:
#     data = json.loads(sys.argv[1])
#     if not isinstance(data, list):
#         raise ValueError("JSON recebido não é uma lista válida.")
# except json.JSONDecodeError:
#     print("Erro ao decodificar JSON. Verifique os dados enviados.")
#     sys.exit(1)

# for event in data:
#     text_content = f"Starlink às {event['Time']}\nDia {event['Date']}\nDuração: {event['Duration']} min\nOlhe de {event['ViewingDirection']['From']} para {event['ViewingDirection']['To']}"





# # Diretórios
# image_folder = 'images'
# output_folder = 'createdImages'
# hash_file = 'posted_images.json'
# os.makedirs(output_folder, exist_ok=True)

# # Carregar histórico de imagens postadas
# if os.path.exists(hash_file) and os.path.getsize(hash_file) > 0:
#     with open(hash_file, 'r') as f:
#         try:
#             posted_hashes = json.load(f)
#         except json.JSONDecodeError:
#             posted_hashes = []
# else:
#     posted_hashes = []


# # Listar imagens disponíveis
# image_files = [f for f in os.listdir(image_folder) if f.startswith('spaceimage')]

# # Fonte para o texto
# font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
# font_size = 36
# font = ImageFont.truetype(font_path, font_size)

# def generate_hash(text):
#     return hashlib.md5(text.encode()).hexdigest()

# # Iterar sobre os eventos recebidos
# for event in json.loads(sys.argv[1]):
#     text_content = f"Starlink às {event['Time']}\nDia {event['Date']}\nDuração: {event['Duration']} min\nOlhe de {event['ViewingDirection']['From']} para {event['ViewingDirection']['To']}"
#     event_hash = generate_hash(text_content)

#     if event_hash in posted_hashes:
#         print(f"Imagem para o evento {event['Time']} já foi postada.")
#         continue

#     # Escolher uma imagem aleatória
#     selected_image = random.choice(image_files)
#     image = Image.open(os.path.join(image_folder, selected_image))
#     draw = ImageDraw.Draw(image)

#     # Colors
#     shadow_color = (0, 0, 0)        # Black shadow
#     outline_color = (0, 0, 0)     # Black outline
#     text_color = (255, 255, 255)    # White text
#     # Adicionar texto
#     draw.text((30, 50), text_content, font=font, fill=(255, 255, 255))
    
#     # Salvar imagem
#     output_path = os.path.join(output_folder, f"image_{event_hash}.jpg")
#     image.save(output_path)

#     # Atualizar histórico de postagens
#     posted_hashes.append(event_hash)
#     with open(hash_file, 'w') as f:
#         json.dump(posted_hashes, f)

#     # Chamar script de postagem
#     subprocess.run(["python3", "postOnInsta.py", output_path])


################################################################################################
######################################################################################
################################################################################################
######################################################################################
################################################################################################
######################################################################################
################################################################################################
######################################################################################
################################################################################################
######################################################################################
################################################################################################
######################################################################################

################################################################################################
######################################################################################
################################################################################################
######################################################################################
################################################################################################
######################################################################################
################################################################################################
######################################################################################
################################################################################################
######################################################################################
################################################################################################
#########################################################

from PIL import Image, ImageDraw, ImageFont
import os
import sys
import random
import hashlib
import json
import subprocess
import dateparser
from datetime import datetime

print("Raw JSON input:", sys.argv[1])  # Depuração

try:
    data = json.loads(sys.argv[1])
    if not isinstance(data, list):
        raise ValueError("JSON recebido não é uma lista válida.")
except json.JSONDecodeError:
    print("Erro ao decodificar JSON. Verifique os dados enviados.")
    sys.exit(1)

# Diretórios
image_folder = 'images'
output_folder = 'createdImages'
hash_file = 'posted_images.json'
os.makedirs(output_folder, exist_ok=True)

# Carregar histórico de imagens postadas
if os.path.exists(hash_file) and os.path.getsize(hash_file) > 0:
    with open(hash_file, 'r') as f:
        try:
            posted_hashes = json.load(f)
        except json.JSONDecodeError:
            posted_hashes = []
else:
    posted_hashes = []

# Listar imagens disponíveis
image_files = [f for f in os.listdir(image_folder) if f.startswith('spaceimage')]

# Fonte para o texto
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font_size = 36
font = ImageFont.truetype(font_path, font_size)

def generate_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

# Iterar sobre os eventos recebidos
for event in data:
    text_content = f"Starlink às {event['Time']}\nDia {event['Date']}\nDuração: {event['Duration']} min\nOlhe de {event['ViewingDirection']['From']} para {event['ViewingDirection']['To']}"
    event_hash = generate_hash(text_content)

    if event_hash in posted_hashes:
        print(f"Imagem para o evento {event['Time']} já foi postada.")
        continue

    # Data e hora do evento
    event_time = event['Time']  
    event_date = event['Date'] 
    raw_datetime = f"{event['Date']} {event['Time']}"
    timedate = dateparser.parse(raw_datetime)

    # Escolher uma imagem aleatória
    selected_image = random.choice(image_files)
    image = Image.open(os.path.join(image_folder, selected_image))
    draw = ImageDraw.Draw(image)

    # Cores
    shadow_color = (0, 0, 0)        # Preto (sombra)
    outline_color = (0, 0, 0)       # Preto (contorno)
    text_color = (255, 255, 255)    # Branco (texto principal)

    # Posição do texto
    position = (30, 50)

    # Adicionar sombra (deslocamento de 2px)
    shadow_offset = 2
    for dx in range(-shadow_offset, shadow_offset + 1):
        for dy in range(-shadow_offset, shadow_offset + 1):
            if dx != 0 or dy != 0:
                draw.text((position[0] + dx, position[1] + dy), text_content, font=font, fill=shadow_color)

    # Adicionar contorno (deslocamento de 1px)
    outline_offset = 1
    for dx in (-outline_offset, 0, outline_offset):
        for dy in (-outline_offset, 0, outline_offset):
            if dx != 0 or dy != 0:
                draw.text((position[0] + dx, position[1] + dy), text_content, font=font, fill=outline_color)

    # Adicionar texto principal
    draw.text(position, text_content, font=font, fill=text_color)

    # Salvar imagem
    output_path = os.path.join(output_folder, f"image_{event_hash}.jpg")
    image.save(output_path)

    # Atualizar histórico de postagens
    posted_hashes.append(event_hash)
    with open(hash_file, 'w') as f:
        json.dump(posted_hashes, f)

    # Chamar script de postagem
    timedate_str = timedate.strftime("%Y-%m-%d_%H-%M-%S")
    subprocess.run(["python3", "postOnInsta.py", output_path, timedate_str ])
