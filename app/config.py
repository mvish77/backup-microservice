from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    """All environment configrurations"""
    PG_HOST = os.getenv("PG_HOST")
    PG_DUMP_PATH = os.getenv("PG_DUMP_PATH")
    PG_PORT = os.getenv("PG_PORT", 5432)
    PG_USER = os.getenv("PG_USER")
    PG_PASSWORD = os.getenv("PG_PASSWORD")
    PG_DATABASE = os.getenv("PG_DATABASE")

    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_ENDPOINT = os.getenv("AWS_ENDPOINT")
    S3_BUCKET = os.getenv("S3_BUCKET")
    S3_REGION = os.getenv("S3_REGION")

    UPLOAD_INTERVAL_MINUTES = int(os.getenv("UPLOAD_INTERVAL_MINUTES", 30))

settings = Settings()
