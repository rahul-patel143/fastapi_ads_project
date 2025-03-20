import logging
import datetime
from apscheduler.schedulers.background import BackgroundScheduler

# Configure logging
logging.basicConfig(
    filename="cron_logs.log",  # Save logs to a file
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

scheduler = BackgroundScheduler()

def log_cron_job():
    """Function that logs execution"""
    log_message = f"Cron job executed at: {datetime.datetime.now()}"
    logging.info(log_message)

def start_scheduler():
    """Start the scheduler automatically"""
    if not scheduler.running:
        scheduler.start()
        scheduler.add_job(log_cron_job, "interval", hours=6, id="log_cron")
        logging.info("Scheduler started & cron job added.")

# Import for Auto-start the scheduler
start_scheduler()
