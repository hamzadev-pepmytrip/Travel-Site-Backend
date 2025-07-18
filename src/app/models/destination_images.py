from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class DestinationImage(Base):
    __tablename__ = "destination_images"

    id = Column(Integer, primary_key=True, index=True)
    destination_id = Column(Integer, ForeignKey("destinations.id", ondelete="CASCADE"), nullable=False, index=True)
    image_url = Column(String(255), nullable=False)

    destination = relationship("Destination", back_populates="images")
    
