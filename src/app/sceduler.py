# app/scheduler.py

from apscheduler.schedulers.background import BackgroundScheduler
from app.database import SessionLocal
from app.models.package import Package
from datetime import date

def deactivate_expired_deals():
    db = SessionLocal()
    try:
        today = date.today()

        expired_deals = db.query(Package).filter(
            Package.on_deal == True,
            Package.deal_end_date < today
        ).all()

        for deal in expired_deals:
            deal.on_deal = False

        db.commit()
    finally:
        db.close()

def start_scheduler():
    scheduler = BackgroundScheduler()
    
    scheduler.add_job(deactivate_expired_deals, 'interval', minutes=10)

    scheduler.start()
