from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.dependencies import get_db
from datetime import date
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




@router.get("/api/deals", response_model=list[PackageOut])
def get_active_deals(db: Session = Depends(get_db)):
    today = date.today()
    deals = db.query(Package).filter(
        Package.on_deal == True,
        Package.deal_start_date <= today,
        Package.deal_end_date >= today,
        Package.is_active == True
    ).all()
    return deals


@router.put("/api/{package_id}", response_model=PackageOut)
def update_package(package_id: int, data: PackageCreate, db: Session = Depends(get_db)):
    package = db.query(Package).get(package_id)
    if not package:
        raise HTTPException(status_code=404, detail="Package not found")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(package, field, value)

    db.commit()
    db.refresh(package)
    return package


@router.put("/api/deal/{package_id}", response_model=PackageOut)
def update_package_deal(package_id: int, data: PackageCreate, db: Session = Depends(get_db)):
    package = db.query(Package).get(package_id)
    if not package:
        raise HTTPException(status_code=404, detail="Package not found")

    package.on_deal = data.on_deal
    package.deal_start_date = data.deal_start_date
    package.deal_end_date = data.deal_end_date

    db.commit()
    db.refresh(package)
    return package


@router.get("/slug/{slug}", response_model=PackageOut)
def get_package_by_slug(slug:str, db: Session = Depends(get_db)):
    package = db.query(Package).filter(Package.slug == slug).first()
    if not package:
        raise HTTPException(status_code=404, detail="Package not found")
    return package