import os, subprocess, datetime, gzip, shutil
from .models import db, BackupLog
BACKUP_DIR = os.getenv('BACKUP_DIR', '/backups')
PG_DUMP_PATH = os.getenv('PG_DUMP_PATH', 'pg_dump')
DB_URL = os.getenv('SOURCE_DB_URL', 'postgresql://user:pass@localhost:5432/db')
def run_backup():
    ts = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')
    filename = f'backup_{ts}.sql'
    dump_path = os.path.join(BACKUP_DIR, filename)
    gz_path = dump_path + '.gz'
    cmd = [PG_DUMP_PATH, '--dbname', DB_URL]
    with open(dump_path, 'wb') as out:
        subprocess.check_call(cmd, stdout=out)
    with open(dump_path, 'rb') as f_in, gzip.open(gz_path, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
    os.remove(dump_path)
    size = os.path.getsize(gz_path)
    log = BackupLog(filename=os.path.basename(gz_path), size_bytes=size)
    db.session.add(log)
    db.session.commit()
    return os.path.basename(gz_path)
