from PIL import Image, ImageDraw, ImageFont
import os
import sys
import random
import hashlib
import json
import subprocess

print("Raw JSON input:", sys.argv[1])  # Depuração

try:
    data = json.loads(sys.argv[1])
    if not isinstance(data, list):
        raise ValueError("JSON recebido não é uma lista válida.")
except json.JSONDecodeError:
    print("Erro ao decodificar JSON. Verifique os dados enviados.")
    sys.exit(1)

for event in data:
    text_content = f"Starlink às {event['Time']}\nDia {event['Date']}\nDuração: {event['Duration']} min\nOlhe de {event['ViewingDirection']['From']} para {event['ViewingDirection']['To']}"





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
for event in json.loads(sys.argv[1]):
    text_content = f"Starlink às {event['Time']}\nDia {event['Date']}\nDuração: {event['Duration']} min\nOlhe de {event['ViewingDirection']['From']} para {event['ViewingDirection']['To']}"
    event_hash = generate_hash(text_content)

    if event_hash in posted_hashes:
        print(f"Imagem para o evento {event['Time']} já foi postada.")
        continue

    # Escolher uma imagem aleatória
    selected_image = random.choice(image_files)
    image = Image.open(os.path.join(image_folder, selected_image))
    draw = ImageDraw.Draw(image)

    # Colors
    shadow_color = (0, 0, 0)        # Black shadow
    outline_color = (0, 0, 0)     # Black outline
    
    # Adicionar texto
    draw.text((30, 50), text_content, font=font, fill=(255, 255, 255))
    
    # Salvar imagem
    output_path = os.path.join(output_folder, f"image_{event_hash}.jpg")
    image.save(output_path)

    # Atualizar histórico de postagens
    posted_hashes.append(event_hash)
    with open(hash_file, 'w') as f:
        json.dump(posted_hashes, f)

    # Chamar script de postagem
    subprocess.run(["python3", "postOnInsta.py", output_path])
