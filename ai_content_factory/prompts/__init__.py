from pathlib import Path

BASE_DIR = Path(__file__).parent

def load_system_prompt() -> str:
    with open(BASE_DIR / "system_prompt.md", "r") as f:
        return f.read()

def load_platform_prompt(platform: str) -> str:
    path = BASE_DIR / f"{platform}.md"
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return ""
