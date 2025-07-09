# src/app/models/destination.py

from sqlalchemy import Column, Integer, String
from app.database import Base

class Destination(Base):
    __tablename__ = "destinations"

    id = Column(Integer, primary_key=True, index=True)
    country_name = Column(String(255), nullable=False)
    region = Column(String(255), nullable=False)
    slug = Column(String(255), unique=True, index=True, nullable=False)
