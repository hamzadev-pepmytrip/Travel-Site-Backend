
from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship

class Region(Base):
    __tablename__ = "regions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)

    destinations = relationship("Destination", back_populates="region")
