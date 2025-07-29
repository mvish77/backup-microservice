import subprocess
import datetime
import os
from .config import settings
from .logger import error,info

def dump_postgres_db():
    """methods to dump database to sql file and return its path with current time stamp"""
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{settings.PG_DATABASE}_backup_{timestamp}.sql"
    output_path = os.path.join(os.getcwd(),"backups", filename)

    cmd = [
        f"{settings.PG_DUMP_PATH}",
        f"--dbname=postgresql://{settings.PG_USER}:{settings.PG_PASSWORD}@{settings.PG_HOST}:{settings.PG_PORT}/{settings.PG_DATABASE}",
        "-f", output_path
    ]

    try:
        subprocess.run(cmd, check=True)
        info(f"Database dumped successfully...")
        return output_path
    except:
        error(f"Database dump failed...")
        return None
