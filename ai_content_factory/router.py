import openai
from .config import get_settings
from .prompts import load_system_prompt, load_platform_prompt
from .schemas import PLATFORM_SCHEMAS

settings = get_settings()
openai.api_key = settings.openai_api_key

async def route_prompt(user_prompt: str, route: str) -> str:
    system = load_system_prompt()
    platform_prompt = load_platform_prompt(route)
    schema = PLATFORM_SCHEMAS.get(route, "")

    prompt = f"""
{system}

{platform_prompt}

User Prompt: {user_prompt}

JSON Schema:
{schema}
"""

    response = await openai.ChatCompletion.acreate(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ]
    )

    return response['choices'][0]['message']['content']
