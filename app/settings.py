from dataclasses import dataclass
from functools import lru_cache
import os
from typing import Optional

from dotenv import load_dotenv

load_dotenv()


def _env_float(key: str, default: float) -> float:
    raw = os.getenv(key)
    if raw is None or raw.strip() == "":
        return default
    try:
        return float(raw)
    except ValueError:
        return default


@dataclass(frozen=True)
class Settings:
    openai_api_key: Optional[str] = os.getenv("OPENAI_API_KEY")
    openai_model: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    openai_base_url: Optional[str] = os.getenv("OPENAI_BASE_URL")
    openai_temperature: float = _env_float("OPENAI_TEMPERATURE", 0.2)


@lru_cache
def get_settings() -> Settings:
    return Settings()
