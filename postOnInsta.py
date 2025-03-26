from instagrapi import Client
import sys
import json
import os
import hashlib
from datetime import datetime

# Arquivo de hashes das imagens já postadas
hash_file = 'posted_images.json'
if os.path.exists(hash_file) and os.path.getsize(hash_file) > 0:
    with open(hash_file, 'r') as f:
        try:
            posted_hashes = json.load(f)
        except json.JSONDecodeError:
            posted_hashes = []
else:
    posted_hashes = []


# Função para calcular o hash do arquivo de imagem
def calculate_image_hash(image_path):
    with open(image_path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

#Credenciais
USERNAME = "***************"
PASSWORD = "***************"

client = Client()
client.login(USERNAME, PASSWORD)

image_path = sys.argv[1]
image_hash = calculate_image_hash(image_path)

# if image_hash in posted_hashes:
#     print("Esta imagem já foi postada. Pulando postagem.")
# else:
#     client.photo_upload_to_story(image_path)
#     client.photo_upload(image_path, caption="Starlink estará visível no céu! 🌌🚀 #Starlink")
#     print("Imagem postada nos stories com sucesso.")
    
#     # Adicionar hash ao histórico de postagens
#     posted_hashes.append(image_hash)
#     with open(hash_file, 'w') as f:
#         json.dump(posted_hashes, f)

#Check if the event wasn't occured yet 
event_date_and_time = sys.argv[2]
event_date_and_time = datetime.strptime(event_date_and_time, "%Y-%m-%d_%H-%M-%S")
now = datetime.now()

if event_date_and_time < now:
    print("The event has already passed.")
else:
    if image_hash in posted_hashes:
        print("Esta imagem já foi postada. Pulando postagem.")
    else:
        client.photo_upload_to_story(image_path)
        client.photo_upload(image_path, caption="Starlink estará visível no céu! 🌌🚀 #Starlink")
        print("Imagem postada nos stories com sucesso.")
    
        # Adicionar hash ao histórico de postagens
        posted_hashes.append(image_hash)
        with open(hash_file, 'w') as f:
            json.dump(posted_hashes, f)

