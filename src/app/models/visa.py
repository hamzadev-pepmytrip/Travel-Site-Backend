from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class VisaType(Base):
    __tablename__ = "visa_types"

    id = Column(Integer, primary_key=True, index=True)
    destination_id = Column(Integer, ForeignKey("destinations.id"), nullable=False)
    
    visa_format = Column(String(255), nullable=False)
    description = Column(String(1000), nullable=True)
    requirements = Column(String(1000), nullable=True)
    processing_time = Column(String(100), nullable=True)
    service_fee = Column(String(100), nullable=True)

    destination = relationship("Destination", back_populates="visa_types")
