"""Simple GPT-based prompt validator."""

import openai
from .config import get_settings

settings = get_settings()
openai.api_key = settings.openai_api_key


async def validate_prompt(prompt: str, schema: dict) -> bool:
    """Return True if the prompt meets quality requirements."""
    query = f"Validate this prompt: {prompt}\nSchema: {schema}"
    try:
        resp = await openai.ChatCompletion.acreate(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": query}],
        )
        content = resp["choices"][0]["message"]["content"].lower()
        return "ok" in content or "valid" in content
    except Exception:
        return False
