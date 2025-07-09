from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.dependencies import get_db
from app.models.package import Package
from app.schemas.packages  import PackageCreate, PackageOut

router= APIRouter()

@router.post("/", response_model=PackageOut)
def create_package(data: PackageCreate, db: Session = Depends(get_db)):
    new_package = Package(**data.dict())
    db.add(new_package)
    db.commit()
    db.refresh(new_package)
    return new_package

@router.get("/", response_model=list[PackageOut])
def get_packages(db: Session = Depends(get_db)):
    return db.query(Package).all()