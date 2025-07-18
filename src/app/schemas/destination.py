from pydantic import BaseModel
from typing import Optional


class RegionOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class DestinationBase(BaseModel):
    country_name: str
    region: Optional[str] 
    slug: str
    city: Optional[str] = None
    description: Optional[str] = None
    airport_code: Optional[str] = None
    airport: Optional[str] = None
    image_url: Optional[str] = None

class DestinationCreate(DestinationBase):
    pass

class DestinationUpdate(BaseModel):
    country_name: Optional[str] = None
    region: Optional[str] = None
    slug: Optional[str] = None
    city: Optional[str] = None
    description: Optional[str] = None
    airport_code: Optional[str] = None
    airport: Optional[str] = None
    image_url: Optional[str] = None

class DestinationOut(DestinationBase):
    id: int
    region: Optional[RegionOut]

    class Config:
        orm_mode = True
