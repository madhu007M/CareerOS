"""
CareerOS Configuration
"""

from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / ".env")


class Settings:
    APP_NAME = "CareerOS"

    VERSION = "1.0.0"

    DEBUG = True

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///careeros.db"
    )

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "CHANGE_ME"
    )


settings = Settings()