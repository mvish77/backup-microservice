import threading
import time
from .upload import dump_postgres_db
from .logger import error,info
from .config import settings
from threading import Lock
import boto3
import os
import shutil

lock = Lock()

def schedule_upload():
    """Creating upload schedule to schedule backup for specific time"""
    while True:

        if lock.locked():
            info("Backup already running, skipping...")
            time.sleep(10)
            continue

        with lock:
            info("Upload schedule started successfully...")
            path = dump_postgres_db()
            if path:
                _upload_to_bucket(path)
        time.sleep(settings.UPLOAD_INTERVAL_MINUTES * 60)

        



def start_background_scheduler():
    """starting thread for auto backup process"""
    thread = threading.Thread(target=schedule_upload, daemon=True)
    thread.start()


def _upload_to_bucket(file_path):
    """Uploads a file to AWS S3 or Cloudflare R2 using boto3 S3 API"""
    session = boto3.session.Session()
    s3 = session.client(
        service_name="s3",
        endpoint_url=settings.AWS_ENDPOINT,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
    )
    file_name = os.path.basename(file_path)
    try:
        uploaded = s3.upload_file(file_path, settings.S3_BUCKET, file_name)
        if uploaded:
            info("Database uploaded successfully...")
            shutil.rmtree(file_path)
            os.remove(file_path)
        else:
            info("Network issue or failed to upload database...")
    except:
        error("Got an error while uploading backup to S3 API...")