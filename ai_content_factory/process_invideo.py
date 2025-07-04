"""Process videos using InVideo AI service."""

import httpx


async def format_video(video_url: str, instructions: str) -> list[str]:
    """Send clip and instructions to InVideo and return formatted URLs."""
    url = "https://api.invideo.io/process"
    json = {"video": video_url, "instructions": instructions}
    async with httpx.AsyncClient() as client:
        try:
            r = await client.post(url, json=json)
            if r.status_code == 200:
                return r.json().get("outputs", [])
        except httpx.HTTPError:
            pass
    return []
