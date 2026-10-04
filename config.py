# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
    MAX_CONCURRENT_JOBS: int = int(os.getenv("MAX_CONCURRENT_JOBS", "2"))
    DOWNLOAD_TIMEOUT: int = int(os.getenv("DOWNLOAD_TIMEOUT", "300"))
    PROCESSING_TIMEOUT: int = int(os.getenv("PROCESSING_TIMEOUT", "120"))
    METADATA_TIMEOUT: int = int(os.getenv("METADATA_TIMEOUT", "30"))
    MAX_FILE_SIZE_MB: int = int(os.getenv("MAX_FILE_SIZE_MB", "50"))
    MAX_FILE_SIZE_BYTES: int = int(os.getenv("MAX_FILE_SIZE_MB", "50")) * 1024 * 1024
    WORK_DIR: str = os.getenv("WORK_DIR", "./temp")
    LOG_DIR: str = os.getenv("LOG_DIR", "./logs")
    YTDLP_RATE_LIMIT: str = os.getenv("YTDLP_RATE_LIMIT", "2M")
    PORT: int = int(os.getenv("PORT", "8080"))
    MAX_VIDEO_DURATION: int = int(os.getenv("MAX_VIDEO_DURATION", "7200"))
    MAX_CLIP_DURATION: int = int(os.getenv("MAX_CLIP_DURATION", "600"))

    @classmethod
    def validate(cls):
        if not cls.BOT_TOKEN:
            raise ValueError("BOT_TOKEN is required")
        os.makedirs(cls.WORK_DIR, exist_ok=True)
        os.makedirs(cls.LOG_DIR, exist_ok=True)

config = Config()
