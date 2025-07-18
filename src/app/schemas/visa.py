from pydantic import BaseModel
from typing import Optional

class VisaBase(BaseModel):
    country_name: str
    visa_type: str
    description: Optional[str] = None
    requirements: Optional[str] = None
    processing_time: Optional[int] = None
    service_fee: Optional[float] = None
    image_url: Optional[str] = None

    class Config:
        orm_mode = True


class VisaCreate (VisaBase):
    pass    

class VisaUpdate(BaseModel): 
    pass

class VisaOut(VisaBase):
    id: int

    class Config:
        orm_mode = True