from datacsv import CSVDatabase
from datetime import datetime
import os

LOG_FILE = "logs.csv"

# Create CSV log schema if not exists
if not os.path.exists(LOG_FILE):
    db = CSVDatabase(LOG_FILE,['timestamp','level','message'])
    db.insert({
        "timestamp": datetime.utcnow().isoformat(),
        "level": "INFO",
        "message": "Log file initialized."
    })

def log(level: str, message: str):
    db = CSVDatabase(LOG_FILE)
    db.insert({
        "timestamp": datetime.utcnow().isoformat(),
        "level": level.upper(),
        "message": message
    })

def info(message: str):
    log("INFO", message)

def error(message: str):
    log("ERROR", message)

def get_logs_to_html():
    db = CSVDatabase(LOG_FILE)
    return db.to_html()

def get_all_logs()->list:
    db = CSVDatabase(LOG_FILE)
    return db.find_all()

def filter_error(level:str)->list:
    db = CSVDatabase(LOG_FILE)
    def filter(row):
        return row['level'] == level
    return db.find_where(filter)