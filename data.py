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


#passar esses dados para o editImage.py 