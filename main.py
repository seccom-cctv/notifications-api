from typing import Union
from fastapi import Depends, FastAPI, HTTPException, Request, Response
from sqlalchemy.orm import Session
#from schemas import UserBase, UserCreate
#import crud, models
from database import SessionLocal, engine
import requests
import os
from dotenv import load_dotenv
import logging


from models import *

#models.Base.metadata.create_all(bind=engine) # create the database tables
app = FastAPI()

# api_url = os.getenv("API_URL")
#API_URL = "http://localhost:8082/v1/internal/device_managers"
API_URL = os.getenv("SITES_API_URL")

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
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


@app.get("/")
async def read_root():
    '''Document endpoint usage here'''

    return {"Hello": "World"}

@app.post("/send")
async def send_notifications(camera_id: int):
    global API_URL

    response = {"msg": []}
    #for user_id in camera_id:
        # Get User preference from db

    url = f'{API_URL}/{camera_id}'

    r = requests.get(url = url)
  
    # extracting data in json format
    data = r.json()
    # print(data)

    # users = data.users  

    #user = crud.get_user(db, user_id=user_id)

    

    for user in data:
        b = True
        print(user)
        logging.info(user)
        for attribute in user["Attributes"]:
            if attribute["Name"]=="email":
                response["msg"].append("dispatch email notification")
                send_email("sinid.lei@gmail.com", "kzwnxvsbvvrhtibm", attribute["Value"], "ALERT DETECTED", "Alert detected in your company.")
                b=False
        if b:
            response["msg"].append(f"User not found")

    return response

# @app.post("/users/", response_model=UserBase)
# def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     return crud.create_user(db=db, user=user)

# @app.get("/users/", response_model=list[UserBase])
# async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     print(users)
#     response = {"users": []}
#     for user in users:
#         print(user)
#         response["users"].append(user)

#     return users



def send_email(user, pwd, recipient, subject, body):
    import smtplib

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = f"From: {FROM}\nTo: {TO}\nSubject: {SUBJECT}\n\n{TEXT}"

    print(message)
    
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login(user, pwd)
    server.sendmail(FROM, TO, message)
    server.close()
    print('successfully sent the mail')

    