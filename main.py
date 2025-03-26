from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import sys
import subprocess
import json

# Configuração do WebDriver
driver = webdriver.Chrome()  # Certifique-se de ter o WebDriver instalado corretamente
driver.get("https://findstarlink.com/#3451668;3")  # Substitua com a URL correta

# Espera para carregar o conteúdo JavaScript
time.sleep(6)  # Ajuste conforme necessário

# Buscar o elemento correto (verifique se o ID está certo)
try:
    # element = driver.find_element(By.ID, "goodTimings")  #COMENTADA QND A VISUALIZAÇÃO ESTIVER BOA EU DESCOMENTO
    element = driver.find_element(By.ID, "avgTimings")
except Exception as e:
    print("Erro ao encontrar o elemento:", e)
    driver.quit()
    exit()

# Lista para armazenar informações
arrayWithAllInformation = []

# Regex patterns
date_time_pattern = r"(\d{1,2}:\d{2} (?:am|pm)), (\d{1,2} \w{3} \d{4})"
duration_pattern = r"for (\d+) mins"
direction_pattern = r"Look from (\w+) to (\w+)"
elevation_pattern = r"Elevation \(from horizon\): start: (\d+)°, max: (\d+)°, end: (\d+)°"

# Extrair informações usando regex
date_time_matches = re.findall(date_time_pattern, element.text)
duration_matches = re.findall(duration_pattern, element.text)
direction_matches = re.findall(direction_pattern, element.text)
elevation_matches = re.findall(elevation_pattern, element.text)

# Armazenar as informações extraídas
for i in range(len(date_time_matches)):
    info = {
        "Time": date_time_matches[i][0],
        "Date": date_time_matches[i][1],
        "Duration": duration_matches[i] if i < len(duration_matches) else "N/A",
        "ViewingDirection": {
            "From": direction_matches[i][0] if i < len(direction_matches) else "N/A",
            "To": direction_matches[i][1] if i < len(direction_matches) else "N/A",
        },
        "Elevation": {
            "Start": elevation_matches[i][0] if i < len(elevation_matches) else "N/A",
            "Max": elevation_matches[i][1] if i < len(elevation_matches) else "N/A",
            "End": elevation_matches[i][2] if i < len(elevation_matches) else "N/A",
        },
    }
    arrayWithAllInformation.append(info)

print(arrayWithAllInformation)
if arrayWithAllInformation == []:
    sys.exit()

# Converter a lista para JSON e passar para o outro script
json_data = json.dumps(arrayWithAllInformation)
subprocess.run(["python", "data.py", json_data])

# Fechar o navegador
driver.quit()
