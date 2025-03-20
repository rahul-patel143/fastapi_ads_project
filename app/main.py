from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import engine, Base
from .dependencies import get_db
from .schemas import MetricsFilter, AdMetricsResponse
from .crud import get_ad_metrics
from .cron_jobs import scheduler

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/ad-metrics", response_model=list[AdMetricsResponse])
def read_ad_metrics(filters: MetricsFilter = Depends(), db: Session = Depends(get_db)):
    return get_ad_metrics(db, filters)

@app.get("/")
def health_check():
    return {"message": "API is running"}

@app.get("/logs")
def get_latest_logs():
    """Fetch the last 10 log lines"""
    try:
        with open("cron_logs.log", "r") as file:
            logs = file.readlines()
        return {"logs": logs[-10:]}  # Return the last 10 logs
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Log file not found")