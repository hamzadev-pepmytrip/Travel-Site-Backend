from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

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
    on_deal: Optional[bool] = False
    deal_start_date: Optional[date] = None
    deal_end_date: Optional[date] = None

class Config:
    orm_mode = True

class PackageCreate(PackageBase):
    pass

class PackageUpdate(PackageBase):
    pass

class PackageDealUpdate(BaseModel):
    on_deal: bool
    deal_start_date: Optional[date] = None
    deal_end_date: Optional[date] = None

class PackageOut(PackageBase):
    id: int
    created_at: datetime
    updated_at: datetime
