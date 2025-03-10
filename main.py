# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import re
# import subprocess

# # Set up Selenium WebDriver
# driver = webdriver.Chrome()  # Use webdriver.Firefox() if using Firefox
# driver.get("https://findstarlink.com/#3451668;3")  # Replace with your actual URL

# # Wait for JavaScript to load the content
# time.sleep(6)  # Adjust sleep time if needed

# # Find the element by class name
# element = driver.find_element(By.ID, "avgTimings") #change for the good visialização later 

# arrayWithAllInformation = []
# #print("Extracted Text:", element.text)


# # Regex patterns
# date_time_pattern = r"(\d{1,2}:\d{2} (?:am|pm)), (\d{1,2} \w{3} \d{4})"
# duration_pattern = r"for (\d+) mins"
# direction_pattern = r"Look from (\w+) to (\w+)"
# elevation_pattern = r"Elevation \(from horizon\): start: (\d+)°, max: (\d+)°, end: (\d+)°"

# # Extract matches
# date_time_matches = re.findall(date_time_pattern, element.text)
# duration_matches = re.findall(duration_pattern, element.text)
# direction_matches = re.findall(direction_pattern, element.text)
# elevation_matches = re.findall(elevation_pattern, element.text)

# arrayWithAllInformation.append(date_time_matches)
# arrayWithAllInformation.append(duration_matches)
# arrayWithAllInformation.append(direction_matches)
# arrayWithAllInformation.append(elevation_matches)

# # Print extracted information
# for i in range(len(date_time_matches)):
#     time, date = date_time_matches[i]
#     duration = duration_matches[i] if i < len(duration_matches) else "N/A"
#     direction_from, direction_to = direction_matches[i] if i < len(direction_matches) else ("N/A", "N/A")
#     elevation_start, elevation_max, elevation_end = elevation_matches[i] if i < len(elevation_matches) else ("N/A", "N/A", "N/A")

#     print(f"Time: {time}, Date: {date}")
#     print(f"Duration: {duration} mins")
#     print(f"Viewing Direction: {direction_from} to {direction_to}")
#     print(f"Elevation: Start {elevation_start}°, Max {elevation_max}°, End {elevation_end}°")
#     print("-" * 50)

# subprocess.run(["python", "test.py", arrayWithAllInformation])






# # Close the browser
# driver.quit()




##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import subprocess
import json

# Configuração do WebDriver
driver = webdriver.Chrome()  # Certifique-se de ter o WebDriver instalado corretamente
driver.get("https://findstarlink.com/#3451668;3")  # Substitua com a URL correta

# Espera para carregar o conteúdo JavaScript
time.sleep(6)  # Ajuste conforme necessário

# Buscar o elemento correto (verifique se o ID está certo)
try:
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

# Exibir as informações extraídas
for item in arrayWithAllInformation:
    print(f"Time: {item['Time']}, Date: {item['Date']}")
    print(f"Duration: {item['Duration']} mins")
    print(f"Viewing Direction: {item['ViewingDirection']['From']} to {item['ViewingDirection']['To']}")
    print(f"Elevation: Start {item['Elevation']['Start']}°, Max {item['Elevation']['Max']}°, End {item['Elevation']['End']}°")
    print("-" * 50)

# Converter a lista para JSON e passar para o outro script
json_data = json.dumps(arrayWithAllInformation)
subprocess.run(["python", "test.py", json_data])

# Fechar o navegador
driver.quit()
