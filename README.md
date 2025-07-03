# AI Content Factory

A minimal Python system to generate social media content with OpenAI GPT and DALL·E 3. Images fall back to Fal.ai and videos can be generated with Veo when available.

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
