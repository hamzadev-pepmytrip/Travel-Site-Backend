from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PackageBase(BaseModel):
    title: str
    slug: str
    description: Optional[str] = None
    price: float
    duration_days: int
    destination_id: int
    category_id: int
    featured: Optional[bool] = False
    image_url: Optional[str] = None
    rating: Optional[float] = None
    is_active: Optional[bool] = True

class PackageCreate(PackageBase):
    pass

class PackageOut(PackageBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
