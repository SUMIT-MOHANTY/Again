from apscheduler.schedulers.background import BackgroundScheduler
from .backup_service import run_backup
def start_scheduler(app):
    scheduler = BackgroundScheduler()
    scheduler.add_job(lambda: app.app_context().push() or run_backup(), 'cron', hour=2, minute=0)
    scheduler.start()
