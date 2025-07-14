from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.dependencies import get_db
from app.models.destination_images import DestinationImage
from app.schemas.destination_images import DestinationImageCreate, DestinationImageOut

router = APIRouter()

@router.post("/", response_model=DestinationImageOut)
def create_destinationImage(date: DestinationImageCreate, db: Session = Depends(get_db)):
    new_destinationImage = DestinationImage(**date.dict())
    db.add(new_destinationImage)
    db.commit()
    db.refresh(new_destinationImage)
    return new_destinationImage


@router.get("/", response_model=list[DestinationImageOut])
def get_destinationImages(db: Session = Depends(get_db)):
    return db.query(DestinationImage).all()