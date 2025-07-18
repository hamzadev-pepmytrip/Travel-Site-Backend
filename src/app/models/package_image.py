from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class PackageImage(Base):
    __tablename__ = "package_images"

    id = Column(Integer, primary_key=True, index=True)
    package_id = Column(Integer, ForeignKey("packages.id", ondelete="CASCADE"), nullable=False, index=True)
    image_url = Column(Text, nullable=False)

    package = relationship("Package", back_populates="images", passive_deletes=True)
