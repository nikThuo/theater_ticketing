from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi_jwt_auth import AuthJWT
from . import models, schemas, database

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(database.get_db), Authorize: AuthJWT = Depends()):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or not pwd_context.verify(user.password, db_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = Authorize.create_access_token(subject=db_user.email)
    return {"access_token": access_token}

@router.get("/me", response_model=schemas.User)
def get_me(Authorize: AuthJWT = Depends(), db: Session = Depends(database.get_db)):
    Authorize.jwt_required()
    current_user_email = Authorize.get_jwt_subject()
    user = db.query(models.User).filter(models.User.email == current_user_email).first()
    return user
