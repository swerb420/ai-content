import httpx
from .config import get_settings

settings = get_settings()

async def send_telegram_message(title: str, message: str) -> None:
    if not (settings.telegram_token and settings.telegram_chat_id):
        return
    url = f"https://api.telegram.org/bot{settings.telegram_token}/sendMessage"
    data = {"chat_id": settings.telegram_chat_id, "text": f"{title}\n\n{message}"}
    async with httpx.AsyncClient() as client:
        try:
            await client.post(url, data=data)
        except httpx.HTTPError:
            pass
