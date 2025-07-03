# AI Content Factory

A minimal Python system to generate social media content with OpenAI GPT and DALL·E 3, with fallback to Fal.ai or Veo.

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

Use `generate_video(prompt)` to create a short clip via Veo if available.
