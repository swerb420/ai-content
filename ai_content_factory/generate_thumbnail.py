"""Create thumbnails using DALL·E 3."""

import openai
from .config import get_settings

settings = get_settings()
openai.api_key = settings.openai_api_key


async def create_thumbnail(prompt: str) -> str | None:
    try:
        resp = await openai.Image.acreate(prompt=prompt, n=1, size="1024x1024")
        return resp["data"][0]["url"]
    except Exception:
        return None
