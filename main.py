from fastapi import FastAPI
from .database import engine, Base
# from .routers import auth, admin, user
from . import auth, admin, user

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])
app.include_router(user.router, prefix="/user", tags=["user"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Theater Ticketing System"}
