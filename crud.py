# from sqlalchemy.orm import Session
# from . import models, schemas
#
# def get_user_by_username(db: Session, username: str):
#     return db.query(models.User).filter(models.User.username == username).first()
#
# def create_user(db: Session, user: schemas.UserCreate):
#     hashed_password = get_password_hash(user.password)
#     db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
#
# def create_theater(db: Session, theater: schemas.TheaterCreate):
#     db_theater = models.Theater(name=theater.name, seats=theater.seats)
#     db.add(db_theater)
#     db.commit()
#     db.refresh(db_theater)
#     return db_theater
#
# def create_seating(db: Session, seating: schemas.SeatingCreate):
#     db_seating = models.Seating(theater_id=seating.theater_id, date=seating.date)
#     db.add(db_seating)
#     db.commit()
#     db.refresh(db_seating)
#     return db_seating
#
# def create_reservation(db: Session, reservation: schemas.ReservationCreate):
#     db_reservation = models.Reservation(seating_id=reservation.seating_id, user_id=reservation.user_id, seat_number=reservation.seat_number)
#     db.add(db_reservation)
#     db.commit()
#     db.refresh(db_reservation)
#     return db_reservation
