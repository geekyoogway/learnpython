import requests
TOKEN = "YOUR TELEGRAM BOT TOKEN"
url = f"https://api.telegram.org/bot6665994599:AAGBibkGvqVuGWy5X1w_TiMfJtmVFZAmkAQ/getUpdates"
print(requests.get(url).json())