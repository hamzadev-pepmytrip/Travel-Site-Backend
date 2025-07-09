from pydantic import BaseModel
from typing import Optional

class DestinationBase(BaseModel):
    country_name: str
    region: str
    slug: str

class DestinationCreate(DestinationBase):
    pass

class DestinationUpdate(BaseModel):
    country_name: Optional[str] = None
    region: Optional[str] = None
    slug: Optional[str] = None

class DestinationOut(DestinationBase):
    id: int

    class Config:
        orm_mode = True
