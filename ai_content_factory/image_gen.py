import requests
import openai
from config import OPENAI_API_KEY, FAL_API_KEY

openai.api_key = OPENAI_API_KEY


def generate_image(prompt: str) -> str:
    if OPENAI_API_KEY:
        try:
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="1024x1024"
            )
            return response['data'][0]['url']
        except Exception:
            pass
    if FAL_API_KEY:
        try:
            url = "https://api.fal.ai/generate"
            headers = {"Authorization": f"Bearer {FAL_API_KEY}"}
            json = {"prompt": prompt}
            r = requests.post(url, headers=headers, json=json)
            if r.ok:
                return r.json().get("url")
        except requests.RequestException:
            pass
    return None

def generate_video(prompt: str) -> str:
    try:
        url = "https://api.veo.ai/v3/generate"
        json = {"prompt": prompt}
        r = requests.post(url, json=json)
        if r.ok:
            return r.json().get("url")
    except requests.RequestException:
        pass
    return None
