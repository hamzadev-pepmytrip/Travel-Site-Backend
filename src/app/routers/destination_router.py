from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.dependencies import get_db
from app.models.destination import Destination
from app.schemas.destination import DestinationCreate, DestinationOut, DestinationUpdate

router = APIRouter()

@router.post("/", response_model=DestinationOut)
def create_destination(data: DestinationCreate, db: Session = Depends(get_db)):
    new_destination = Destination(**data.dict())
    db.add(new_destination)
    db.commit()
    db.refresh(new_destination)
    return new_destination



@router.get("/", response_model=list[DestinationOut])
def get_destinations(db: Session = Depends(get_db)):
    return db.query(Destination).all()



@router.put("/{destination_id}", response_model=DestinationOut)
def update_destination(destination_id: int, data: DestinationUpdate, db: Session = Depends(get_db)):
    destination = db.query(Destination).get(destination_id)
    if not destination:
        raise HTTPException(status_code=404, detail="Destination not found")

    for field, value in data.dict(exclude_unset=True).items():
        setattr(destination, field, value)

    db.commit()
    db.refresh(destination)
    return destination
