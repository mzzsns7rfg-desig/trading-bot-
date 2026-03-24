import requests
import time

TOKEN = "8785869904:AAEUaUSOMlo5obHUby88piXgm5GlrzrlHTg"
CHAT_ID = "8507133364"

def send(msg):
    url = "https://api.telegram.org/bot" + TOKEN + "/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

while True:
    send("BOT ONLINE 🚀")
    time.sleep(60)
