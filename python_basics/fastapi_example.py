from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Randomizer API"}

@app.get("/random-number")
def generate_random_number():
    return random.randint(1, 100)

@app.get("/print-message")
def generate_message(message1: str, message2: str):
    return " ".join([message1, message2])

users = [{"user_id": 1, "name": "Alice"}, {"user_id": 2, "name": "Bob"}, {"user_id": 3, "name": "Charlie"}]

@app.get("/users/{user_id}")
def get_users(user_id: int):
    user = next((user for user in users if user["user_id"] == user_id), None)
    if user:
        return user
    return {"error": "User not found"}

@app.post("/user")
def create_user(user: dict):
    users.append(user)
    return {"message": "User created successfully", "user": user}