
from sqlalchemy import Column, Integer, String
from app.database import Base

class PackageCategory(Base):
    __tablename__ = "package_categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    slug = Column(String(100), unique=True, nullable=False)
