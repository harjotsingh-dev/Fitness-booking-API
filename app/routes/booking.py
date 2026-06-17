from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.models import FitnessClass, Booking
from app.schemas.booking import BookingCreate
from app.dependencies import get_db, get_current_user

router = APIRouter()


@router.post("/book")
def book(data: BookingCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):

    cls = db.query(FitnessClass).filter(FitnessClass.id == data.class_id).first()

    if not cls:
        raise HTTPException(status_code=400, detail="class not found")

    if cls.availableSlots <= 0:
        raise HTTPException(status_code=400, detail="No slots available")

    existing = db.query(Booking).filter(
        Booking.class_id == data.class_id,
        Booking.user_id == user.id
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Already booked")

    cls.availableSlots -= 1
    db.add(cls)

    booking = Booking(**data.dict(), user_id=user.id)
    db.add(booking)

    db.commit()

    return {"message": "Booked"}


@router.get("/bookings")
def my_bookings(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return user.bookings