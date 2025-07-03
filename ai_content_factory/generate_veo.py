"""Interact with Google Veo 3 via HTTP API."""

import httpx


async def generate_video(prompt: str) -> str | None:
    """Request a video clip from Veo."""
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
