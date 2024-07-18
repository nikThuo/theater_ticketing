from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    reservations: List["Reservation"] = []

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: str
    password: str

class TheaterBase(BaseModel):
    name: str
    location: str

class TheaterCreate(TheaterBase):
    pass

class Theater(TheaterBase):
    id: int
    seats: List["Seat"] = []

    class Config:
        orm_mode = True

class SeatBase(BaseModel):
    seat_number: str
    theater_id: int

class SeatCreate(SeatBase):
    pass

class Seat(SeatBase):
    id: int
    is_reserved: bool
    reservations: List["Reservation"] = []

    class Config:
        orm_mode = True

class ReservationBase(BaseModel):
    user_id: int
    seat_id: int
    reservation_time: datetime

class ReservationCreate(ReservationBase):
    pass

class Reservation(ReservationBase):
    id: int
    user: User
    seat: Seat

    class Config:
        orm_mode = True
