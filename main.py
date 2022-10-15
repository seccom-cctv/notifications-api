from typing import Union
from fastapi import FastAPI, HTTPException

app = FastAPI()

users = {"User1": ["email"], "User2": ["phone", "email"]}


@app.get("/")
async def read_root():
    '''Document endpoint usage here'''

    return {"Hello": "World"}

@app.post("/send")
async def send_notifications(users_ids=[]):
    print(users_ids)
    print("AAA")
    for user_id in users_ids:
        # Get User preference from db
        
        for preference in users[user_id]:
            if preference == "email":
                print("despatch email notification")
            elif preference == "phone":
                print("despatch SMS notification")





    return users_ids