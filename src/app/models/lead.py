# src/app/models/lead.py

from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.sql import func
from app.database import Base

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255))
    email = Column(String(255))
    phone = Column(String(20))
    interested_in = Column(String(100))
    message = Column(Text)
    source = Column(String(50))
    created_at = Column(TIMESTAMP, server_default=func.now())
