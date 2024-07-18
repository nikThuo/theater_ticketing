from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas, database

router = APIRouter()

@router.get("/theaters/", response_model=List[schemas.Theater])
def list_theaters(db: Session = Depends(database.get_db)):
    return db.query(models.Theater).all()

@router.get("/seats/", response_model=List[schemas.Seat])
def list_seats(theater_id: int, db: Session = Depends(database.get_db)):
    return db.query(models.Seat).filter(models.Seat.theater_id == theater_id, models.Seat.is_reserved == False).all()

@router.post("/reservations/", response_model=schemas.Reservation)
def create_reservation(reservation: schemas.ReservationCreate, db: Session = Depends(database.get_db)):
    db_reservation = models.Reservation(user_id=reservation.user_id, seat_id=reservation.seat_id, reservation_time=reservation.reservation_time)
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation
