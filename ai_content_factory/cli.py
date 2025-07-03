"""Command line interface for end-to-end content generation."""

import asyncio
import typer
from .controller import refine_prompt
from .generate_veo import generate_video
from .process_invideo import format_video
from .generate_thumbnail import create_thumbnail
from .uploader import upload_youtube, upload_tiktok
from .storage import save_record

app = typer.Typer()


@app.command()
def generate_content(idea: str):
    """Run a full content cycle."""
    async def _run() -> None:
        prompts = await refine_prompt(idea)
        video = await generate_video(prompts["veo"])
        formats = await format_video(video or "", prompts["invideo"])
        thumb = await create_thumbnail(prompts["dalle"])
        for url in formats:
            await upload_youtube(url, idea)
            await upload_tiktok(url, idea)
        save_record({"idea": idea, "video": video, "thumb": thumb})
    asyncio.run(_run())


if __name__ == "__main__":
    app()
