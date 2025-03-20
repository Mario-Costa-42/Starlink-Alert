import sys
import json

if len(sys.argv) > 1:
    try:
        arrayWithAllInformation = json.loads(sys.argv[1])
        # print(f"Informações recebidas:\n{json.dumps(arrayWithAllInformation, indent=4)}")
        print("Os dados foram recebidos com sucesso!")
    except json.JSONDecodeError:
        print("Erro ao decodificar os dados JSON recebidos.")
else:
    print("Nenhum dado recebido.")


print("pronto para trabalhar com o sdados")

# Extract data
time = arrayWithAllInformation[0]['Time']
date = arrayWithAllInformation[0]['Date']
duration = arrayWithAllInformation[0]['Duration']
viewing_from = arrayWithAllInformation[0]['ViewingDirection']['From']
viewing_to = arrayWithAllInformation[0]['ViewingDirection']['To']
elevation_start = arrayWithAllInformation[0]['Elevation']['Start']
elevation_max = arrayWithAllInformation[0]['Elevation']['Max']
elevation_end = arrayWithAllInformation[0]['Elevation']['End']

# Print extracted data
print("Time:", time)
print("Date:", date)
print("Duration:", duration)
print("Viewing From:", viewing_from)
print("Viewing To:", viewing_to)
print("Elevation Start:", elevation_start)
print("Elevation Max:", elevation_max)
print("Elevation End:", elevation_end)

































































#passar esses dados para o editImage.py 