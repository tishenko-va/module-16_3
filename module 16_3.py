import asyncio
from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_main_page() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def post_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', examples='Valery')],
        age: int = Path(ge=18, le=120, description="Enter age", examples='55')) -> dict:
    user_id = str(int(max(users, key=int)) + 1)
    new_user = f"Имя: {username}, возраст: {age}"
    users[user_id] = new_user
    return {"message": f"User {user_id} is registered"}


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int,
                      username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', examples='Valery')],
                      age: int = Path(ge=18, le=120, description="Enter age", examples='55'))-> dict:
    update = f"Имя: {username}, возраст: {age}"
    users[user_id] = update
    return {'message': f'The user {user_id} is updated'}


@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    users.pop(user_id)


