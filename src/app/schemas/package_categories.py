from pydantic import BaseModel

class PackageCategoryBase(BaseModel):
    name: str
    slug: str


class PackageCategoryCreate(PackageCategoryBase):
    pass

class PackageCategoryOut(PackageCategoryBase):
    id: int

    class Config:
        orm_mode = True