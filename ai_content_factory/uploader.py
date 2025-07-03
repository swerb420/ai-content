"""Upload generated media to various platforms."""

import httpx


async def upload_youtube(video_url: str, description: str) -> bool:
    url = "https://api.youtube.com/upload"
    json = {"video": video_url, "description": description}
    async with httpx.AsyncClient() as client:
        try:
            r = await client.post(url, json=json)
            return r.status_code == 200
        except httpx.HTTPError:
            return False


async def upload_tiktok(video_url: str, description: str) -> bool:
    url = "https://api.tiktok.com/upload"
    json = {"video": video_url, "description": description}
    async with httpx.AsyncClient() as client:
        try:
            r = await client.post(url, json=json)
            return r.status_code == 200
        except httpx.HTTPError:
            return False
