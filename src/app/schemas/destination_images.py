from pydantic import BaseModel

class DestinationImageBase(BaseModel):
    destination_id: int
    image_url: str

class DestinationImageCreate(DestinationImageBase):
    pass

class DestinationImageOut(DestinationImageBase):
    id: int

    class Config:
        orm_mode = True