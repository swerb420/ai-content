from pydantic import BaseSettings

class Settings(BaseSettings):
    """Configuration loaded from environment variables."""

    openai_api_key: str
    telegram_token: str | None = None
    telegram_chat_id: str | None = None
    fal_api_key: str | None = None

    class Config:
        env_prefix = ""
        env_file = ".env"

def get_settings() -> Settings:
    return Settings()  # type: ignore[arg-type]
