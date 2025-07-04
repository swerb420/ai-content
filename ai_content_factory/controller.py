"""Controller for refining prompts into video and image tasks."""

import openai
from .config import get_settings
from .prompt_validator import validate_prompt

settings = get_settings()
openai.api_key = settings.openai_api_key


async def refine_prompt(idea: str) -> dict:
    """Return structured prompts for Veo, InVideo and DALL-E."""
    base_prompt = f"Refine the following idea into prompts for Veo, InVideo and DALLE.\nIdea: {idea}"
    response = await openai.ChatCompletion.acreate(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": base_prompt}],
    )
    content = response["choices"][0]["message"]["content"]
    prompts = {
        "veo": content,
        "invideo": content,
        "dalle": content,
    }
    for key, value in prompts.items():
        if not await validate_prompt(value, {}):
            prompts[key] = value.strip()
    return prompts
