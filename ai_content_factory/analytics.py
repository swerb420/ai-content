"""Basic analytics utilities."""

import httpx


async def fetch_stats(video_id: str) -> dict:
    url = f"https://api.example.com/stats/{video_id}"
    async with httpx.AsyncClient() as client:
        try:
            r = await client.get(url)
            if r.status_code == 200:
                return r.json()
        except httpx.HTTPError:
            pass
    return {}
