import sys
import json
import subprocess
from deep_translator import GoogleTranslator

if len(sys.argv) > 1:
    try:
        arrayWithAllInformation = json.loads(sys.argv[1])
        # print(f"Informações recebidas:\n{json.dumps(arrayWithAllInformation, indent=4)}")
        # print("Os dados foram recebidos com sucesso!")
    except json.JSONDecodeError:
        print("Erro ao decodificar os dados JSON recebidos.")
else:
    print("Nenhum dado recebido.")


# Extract data
time = arrayWithAllInformation[0]['Time']
date = arrayWithAllInformation[0]['Date']
duration = arrayWithAllInformation[0]['Duration']
viewing_from = arrayWithAllInformation[0]['ViewingDirection']['From']
viewing_to = arrayWithAllInformation[0]['ViewingDirection']['To']


#variables for verification to the datetime
EventDateAndTime = date + " " + time 

date = GoogleTranslator(source='en', target='pt').translate(date)
cardeal1 =  GoogleTranslator(source='en', target='pt').translate(viewing_from)
cardeal2 =  GoogleTranslator(source='en', target='pt').translate(viewing_to)


# export the data
#subprocess.run(["python3", "editImage.py", time, date, duration, cardeal1, cardeal2, EventDateAndTime])

























event_data = json.dumps([
    {
        "Time": time,
        "Date": date,
        "Duration": duration,
        "ViewingDirection": {
            "From": cardeal1,
            "To": cardeal2
        }
    }
])

subprocess.run(["python3", "editImage.py", event_data])




