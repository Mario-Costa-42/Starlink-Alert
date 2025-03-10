# from bs4 import BeautifulSoup
# import requests

# html_text = requests.get('https://findstarlink.com/#3451668;3').text
# soup = BeautifulSoup(html_text, 'lxml')



# resultBox = soup.find_all('div', id = 'goodTimingsBlock')
# print(resultBox)

# resultBoxAvarege = soup.find_all('div', id = 'avgTimingsBlock')
# print(resultBoxAvarege)

# import sys

# if len(sys.argv) > 1:
#     arrayWithAllInformation = sys.argv[1]
#     print(f"the information was received {arrayWithAllInformation}")
# else:
#     print("No data received.")













import sys
import json

if len(sys.argv) > 1:
    try:
        arrayWithAllInformation = json.loads(sys.argv[1])
        print(f"Informações recebidas:\n{json.dumps(arrayWithAllInformation, indent=4)}")
    except json.JSONDecodeError:
        print("Erro ao decodificar os dados JSON recebidos.")
else:
    print("Nenhum dado recebido.")
