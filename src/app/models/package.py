
from sqlalchemy import Column, Integer, String, Text, DECIMAL, Boolean, ForeignKey, TIMESTAMP, Date
from sqlalchemy.sql import func
from app.database import Base
from sqlalchemy.orm import relationship

class Package(Base):
    __tablename__ = "packages"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    slug = Column(String(100), unique=True, index=True, nullable=False)
    description = Column(Text)
    price = Column(DECIMAL(10, 2))
    duration_days = Column(Integer)
    destination_id = Column(Integer, ForeignKey("destinations.id"), index=True)
    category_id = Column(Integer, ForeignKey("package_categories.id"), index=True)
    featured = Column(Boolean, default=False)
    image_url = Column(Text)
    rating = Column(DECIMAL(3, 1))  # If ratings can go up to 10.0
    is_active = Column(Boolean, default=True)
    on_deal = Column(Boolean, default=False)
    deal_start_date = Column(Date)
    deal_end_date = Column(Date)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    category = relationship("PackageCategory", back_populates="packages")
    destination = relationship("Destination", back_populates="packages")
    images = relationship("PackageImage", back_populates="package", cascade="all, delete-orphan")
