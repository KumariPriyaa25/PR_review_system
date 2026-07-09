import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_ENV = os.getenv("APP_ENV", "local")
    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = int(os.getenv("PORT", 8000))

    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    GITHUB_REPO_OWNER = os.getenv("GITHUB_REPO_OWNER")
    GITHUB_TEST_REPO = os.getenv("GITHUB_TEST_REPO")
    GITHUB_WEBHOOK_SECRET = os.getenv("GITHUB_WEBHOOK_SECRET")

    HF_API_TOKEN = os.getenv("HF_API_TOKEN")

settings = Settings()