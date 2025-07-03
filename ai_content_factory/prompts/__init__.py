def load_system_prompt() -> str:
    with open("ai_content_factory/prompts/system_prompt.md", "r") as f:
        return f.read()

def load_platform_prompt(platform: str) -> str:
    path = f"ai_content_factory/prompts/{platform}.md"
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return ""
