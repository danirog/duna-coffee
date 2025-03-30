from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    email: str
    full_name: str = None
    
users_db = {}

@app.post("/users/", response_model=User)
def create_user(user: User):
    if user.id in users_db:
        raise HTTPException(status_code=400, detail="User already exists.")
    users_db[user.id] = user
    return user

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found.")
    return users_db[user_id]

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found.")
    users_db[user_id] = user
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found.")
    del users_db[user_id]
    return {"detail": "User deleted successfully."}