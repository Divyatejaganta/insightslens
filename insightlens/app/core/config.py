from pathlib import Path
from pydantic import BaseModel
import os

class Settings(BaseModel):
    data_dir: Path = Path(os.getenv("INSIGHTLENS_DATA_DIR", ".insightlens"))
    embed_model: str = os.getenv("OPENAI_EMBED_MODEL", "text-embedding-3-small")
    chat_model: str = os.getenv("OPENAI_CHAT_MODEL", "gpt-4o-mini")
    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")

settings = Settings()
settings.data_dir.mkdir(parents=True, exist_ok=True)
(settings.data_dir / "indices").mkdir(parents=True, exist_ok=True)
(settings.data_dir / "datasets").mkdir(parents=True, exist_ok=True)
