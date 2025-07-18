from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Destination(Base):
    __tablename__ = "destinations"

    id = Column(Integer, primary_key=True, index=True)
    region_id = Column(Integer, ForeignKey("regions.id"), index=True)
    country_name = Column(String(255), nullable=False)
    city = Column(String(255), nullable=True)
    slug = Column(String(255), unique=True, index=True, nullable=False)
    description = Column(Text, nullable=True)
    airport_code = Column(String(10), nullable=True)
    airport = Column(String(255), nullable=True)
    image_url = Column(String(255), nullable=True)

    region = relationship("Region", back_populates="destinations")
    visa_types = relationship("VisaType", back_populates="destination", cascade="all, delete-orphan")
    images = relationship("DestinationImage", back_populates="destination", cascade="all, delete-orphan")
    packages = relationship("Package", back_populates="destination", cascade="all, delete-orphan")



