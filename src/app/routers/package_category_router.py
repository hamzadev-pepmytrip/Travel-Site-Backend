from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.dependencies import get_db
from app.models.package_category import PackageCategory
from app.schemas.package_categories import PackageCategoryCreate, PackageCategoryOut

router = APIRouter()

@router.post("/", response_model=PackageCategoryOut)
def create_packageCategory(data: PackageCategoryCreate, db: Session = Depends(get_db)):
    new_packageCategory = PackageCategory(**data.dict())
    db.add(new_packageCategory)
    db.commit()
    db.refresh(new_packageCategory)
    return new_packageCategory

@router.get("/", response_model=list[PackageCategoryOut])
def get_packageCategories(db: Session = Depends(get_db)):
    return db.query(PackageCategory).all()