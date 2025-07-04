# AI Content Factory


## Quick Start

1. Install dependencies:
   ```bash
   pip install -r ai_content_factory/requirements.txt
   ```
2. Set environment variables for API keys:
   - `OPENAI_API_KEY`
   - `TELEGRAM_TOKEN`
   - `TELEGRAM_CHAT_ID`
   - `FAL_API_KEY` (optional)
3. Run the FastAPI app:
   ```bash
   uvicorn ai_content_factory.main:app --reload
   ```

### Repository Structure

All source files live under the `ai_content_factory/` package. Keeping the code
in one directory avoids duplicate modules and simplifies imports.


Send a POST request to `/generate-content` with JSON:
```json
{
  "prompt": "Write a post about AI",
  "route": "linkedin",
  "image_prompt": "robot at desk"
}
```

### Video Generation

`generate_video(prompt)` asynchronously requests a short clip from Veo.

### New Features

- Fully asynchronous HTTP calls
- Environment settings loaded via Pydantic
- Fallback image and video generation endpoints
- Prompts loaded relative to the package for easy deployment


## Advanced Pipeline

This project includes optional modules for a complete video pipeline using Google Veo 3 and InVideo AI. The main steps are:

1. `controller.refine_prompt` turns a content idea into prompts for Veo, InVideo and DALL·E 3.
2. `generate_veo.generate_video` creates a short clip from Veo.
3. `process_invideo.format_video` trims and formats the clip for multiple platforms.
4. `generate_thumbnail.create_thumbnail` generates thumbnails with DALL·E 3.
5. `uploader.upload_youtube` and `uploader.upload_tiktok` publish the videos.
6. `analytics.fetch_stats` can pull performance data for feedback.

Run the CLI with Typer:
```bash
python -m ai_content_factory.cli generate-content "Awesome video idea"
```
