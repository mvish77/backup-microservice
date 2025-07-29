# 🛡️ Backup Microservice

A lightweight, OS-independent microservice built with **FastAPI** that automates **PostgreSQL database backups** and uploads them to **Amazon S3 or Cloudflare R2**. It features real-time logging using the `datacsv` module and supports both scheduled and manual backups.

---

## 🚀 Features

- 🔁 Automatic backup at fixed intervals (configurable via `.env`)
- 🗃️ Uploads to Amazon S3 or Cloudflare R2
- ⚙️ Cross-platform PostgreSQL dumping
- 📦 Uses [datacsv](https://pypi.org/project/datacsv/) for lightweight CSV-based logging
- 📡 FastAPI with endpoints for manual trigger and viewing logs
- ✅ Proper lock mechanism to avoid duplicate backups

---

## 🧱 Folder Structure
```
backup-microservice/
├── app/
│ ├── config.py
│ ├── logger.py
│ ├── upload.py
│ ├── scheduler.py
│ ├── routes.py
├── main.py
├── .env
├── requirements.txt
└── logs.csv
```

---

## 🔧 .env Configuration

1. Create a `.env` file in the root directory.
2. Add the following environment variables:

```env
# ========================== AWS CONFIGURATION ===================================

# YOUR AWS OR CLOUDFLARE KEY ID
AWS_ACCESS_KEY_ID=rv05er45f4318940we84df2b4a1c6e44
# YOUR AWS OR CLOUDFLARE SECRET KEY
AWS_SECRET_ACCESS_KEY=81ew54e96d8a51ac314df298abwe54de781aa6da57we544036c0fb634454ew78
# set your AWS S3 Endpoint or R2 Storage endpoint
AWS_ENDPOINT=https://111111ff25e44a65e749e3fde0bwe548.r2.cloudflarestorage.com
# BUCKET NAME 
S3_BUCKET=db_backup
# SET AUTO FOR R2 BUCKET OR REGION FOR AWS
S3_REGION=AUTO

# ============== POSTGRSQL CONFIGURATION =======================

# FULL PATH OF PostgreSQL pg_dump.exe
PG_DUMP_PATH=C:/Program Files/PostgreSQL/17/bin/pg_dump.exe
# YOUR POSTGRES HOST. DEFAULT TO LOCALHOST
PG_HOST=localhost
# POSTGRES PORT. DEFAULT TO 5432
PG_PORT=5432
# YOUR POSTGRES LOGIN USER
PG_USER=your_postgres_user
# YOUR POSTGRES LOGIN PASSWORD
PG_PASSWORD=your_postgres_password
# YOUR POSTGRES DATABASE
PG_DATABASE=your_postgres_database

# ================ UPLOAD SETTINGS ==============================

# UPLOAD CONFIGURATION DEFAULT IS 30 MIN 1 = 1 MINUTE
UPLOAD_INTERVAL_MINUTES=30
```
✅ You can generate these AWS credentials from your AWS IAM or Cloudflare R2 API panel


## 🛠 Installation & Setup
```bash
# Clone the repository
git clone https://github.com/mvish77/backup-microservice.git
cd backup-microservice

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```
---

## ⚙️ Usage
### ▶️ Run the microservice
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## 📡 API Endpoints
| Method | Endpoint    | Description                     |
| ------ | ----------- | ------------------------------- |
| GET    | `/`         | Health check                    |
| GET    | `/run-once` | Manually trigger backup         |
| GET    | `/logs`     | View real-time logs (CSV-based) |


## 🔒 Preventing Duplicate Backups
* A built-in threading.Lock() mechanism ensures that:
* Background scheduler does not run while a manual backup is in progress
* Manual trigger will skip if the system is already backing up

## ✅ Dependencies
* FastAPI
* datacsv (custom logging)
* python-dotenv
* boto3 (for S3/R2 support)

## 📜 License
MIT License
