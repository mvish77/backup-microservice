from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.logger import get_logs_to_html
from app.scheduler import _upload_to_bucket, start_background_scheduler
from app.upload import dump_postgres_db
from app.config import settings
from app.scheduler import lock

app = FastAPI(title="Database Upload Microservice")

templates = Jinja2Templates(directory='templates')

@app.get("/")
def health_check():
    return {"status": "PG Upload Microservice Running..."}

@app.get("/run-once")
def manual_upload():
    if lock.locked():
        return {"status": "Backup already in progress..."}
    with lock:
        path = dump_postgres_db()
        if path:
            _upload_to_bucket(path)
        return {"status": "Mannual backup completed..."}


@app.get("/logs", response_class=HTMLResponse)
def get_logs(request:Request):
    return templates.TemplateResponse('home.html',{'request':request, "title":f"All logs for {settings.PG_DATABASE}","logs":get_logs_to_html()})

start_background_scheduler()