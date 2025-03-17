from instagrapi import Client

client = Client()

USERNAME = "**********"
PASSWORD = "**********"

client.login(USERNAME, PASSWORD)

try:
    user_info = client.account_info()
    print(f"Logged in as: {user_info.username}")
except Exception:
    print("Not logged in.")



#this code is working but I need to edit the image before 
#posting it on instagram story 