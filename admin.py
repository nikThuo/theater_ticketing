from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas, database

router = APIRouter()

@router.post("/theaters/", response_model=schemas.Theater)
def create_theater(theater: schemas.TheaterCreate, db: Session = Depends(database.get_db)):
    db_theater = models.Theater(name=theater.name, location=theater.location)
    db.add(db_theater)
    db.commit()
    db.refresh(db_theater)
    return db_theater

@router.post("/seats/", response_model=schemas.Seat)
def create_seat(seat: schemas.SeatCreate, db: Session = Depends(database.get_db)):
    db_seat = models.Seat(seat_number=seat.seat_number, theater_id=seat.theater_id)
    db.add(db_seat)
    db.commit()
    db.refresh(db_seat)
    return db_seat

@router.get("/reservations/", response_model=List[schemas.Reservation])
def list_reservations(db: Session = Depends(database.get_db)):
    return db.query(models.Reservation).all()
