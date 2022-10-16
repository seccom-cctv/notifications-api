from typing import Union
from fastapi import Depends, FastAPI, HTTPException, Request, Response
from sqlalchemy.orm import Session
from schemas import UserBase, UserCreate
import crud, models
from database import SessionLocal, engine


from models import *

models.Base.metadata.create_all(bind=engine) # create the database tables
app = FastAPI()

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def read_root():
    '''Document endpoint usage here'''

    return {"Hello": "World"}

@app.post("/send")
async def send_notifications(users_ids: list[int], db: Session = Depends(get_db)):
    print(users_ids)
    response = {"msg": []}
    for user_id in users_ids:
        # Get User preference from db

        user = crud.get_user(db, user_id=user_id)

        if user:
            print(user)
            preference = user.contact_preference
            print(preference)

            if preference == "email":
                response["msg"].append("dispatch email notification")
            elif preference == "phone":
                response["msg"].append("dispatch SMS notification")
        else:
            response["msg"].append(f"User {user_id} not found")

    return response

@app.post("/users/", response_model=UserBase)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)