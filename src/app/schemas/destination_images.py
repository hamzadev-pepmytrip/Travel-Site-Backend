from pydantic import BaseModel, HttpUrl

class DestinationImageBase(BaseModel):
    destination_id: int
    image_url: HttpUrl

class DestinationImageCreate(DestinationImageBase):
    pass

class DestinationImageOut(DestinationImageBase):
    id: int

    class Config:
        orm_mode = True
