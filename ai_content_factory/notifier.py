import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID

def send_telegram_message(title: str, message: str) -> None:
    if not (TELEGRAM_TOKEN and TELEGRAM_CHAT_ID):
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": f"{title}\n\n{message}"}
    try:
        requests.post(url, data=data)
    except requests.RequestException:
        pass
