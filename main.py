import sre_compile
from typing import Union, List
from fastapi import FastAPI, HTTPException
from schema import UserList, ItemList

app = FastAPI()

users = {"User1": ["email"], "User2": ["phone", "email"]}


@app.get("/")
async def read_root():
    '''Document endpoint usage here'''

    return {"Hello": "World"}

@app.post("/send")
async def send_notifications(users_ids: list[str]):
    print(users_ids)
    for user_id in users_ids:
        # Get User preference from db
        preferences = users[user_id]


        for preference in preferences:
            if preference == "email":
                print("dispatch email notification")
            elif preference == "phone":
                print("dispatch SMS notification")

    return users_ids