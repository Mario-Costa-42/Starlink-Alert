from instagrapi import Client
import sys
from datetime import datetime

client = Client()

USERNAME = "**********"
PASSWORD = "**********"


# client.login(USERNAME, PASSWORD)

# try:
#     user_info = client.account_info()
#     print(f"Logged in as: {user_info.username}")
# except Exception:
#     print("Not logged in.")

#Handleing the date and time 
event_date_and_time = datetime.strptime(sys.argv[1], "%d %b %Y %I:%M %p")
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

























