from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.dependencies import get_db
from app.models.visa import VisaType
from app.schemas.visa import VisaCreate, VisaOut

router = APIRouter(prefix="/visa-types", tags=["Visa Types"])


@router.post("/", response_model=VisaOut)
def create_visa_type(data: VisaCreate, db: Session = Depends(get_db)):
    new_visa_type = VisaType(**data.dict())
    db.add(new_visa_type)
    db.commit()
    db.refresh(new_visa_type)
    return new_visa_type


@router.get("/", response_model=list[VisaOut])
def get_visa_types(db: Session = Depends(get_db)):
    return db.query(VisaType).all()


@router.get("/{visa_id}", response_model=VisaOut)
def get_visa_type(visa_id: int, db: Session = Depends(get_db)):
    visa_type = db.query(VisaType).filter(VisaType.id == visa_id).first()
    if not visa_type:
        raise HTTPException(status_code=404, detail="Visa Type not found")
    return visa_type


@router.put("/{visa_id}", response_model=VisaOut)
def update_visa_type(visa_id: int, data: VisaCreate, db: Session = Depends(get_db)):
    visa_type = db.query(VisaType).filter(VisaType.id == visa_id).first()
    if not visa_type:
        raise HTTPException(status_code=404, detail="Visa Type not found")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(visa_type, field, value)

    db.commit()
    db.refresh(visa_type)
    return visa_type
