import openai
import httpx
from config import get_settings

settings = get_settings()
openai.api_key = settings.openai_api_key


async def generate_image(prompt: str) -> str | None:
    if settings.openai_api_key:
        try:
            response = await openai.Image.acreate(
                prompt=prompt,
                n=1,
                size="1024x1024",
            )
            return response['data'][0]['url']
        except Exception:
            pass
    if settings.fal_api_key:
        url = "https://api.fal.ai/generate"
        headers = {"Authorization": f"Bearer {settings.fal_api_key}"}
        json = {"prompt": prompt}
        async with httpx.AsyncClient() as client:
            try:
                r = await client.post(url, headers=headers, json=json)
                if r.status_code == 200:
                    return r.json().get("url")
            except httpx.HTTPError:
                pass
    return None

async def generate_video(prompt: str) -> str | None:
    url = "https://api.veo.ai/v3/generate"
    json = {"prompt": prompt}
    async with httpx.AsyncClient() as client:
        try:
            r = await client.post(url, json=json)
            if r.status_code == 200:
                return r.json().get("url")
        except httpx.HTTPError:
            pass
    return None
