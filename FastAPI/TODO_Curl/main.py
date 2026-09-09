from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import List

app = FastAPI()

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE = timedelta(minutes=5)

class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False

class Login(BaseModel):
    username: str
    password: str

todos: List[Todo] = []

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + ACCESS_TOKEN_EXPIRE

    to_encode.update({
        "exp": expire
    })

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return username

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Token expired or invalid"
        )

@app.get("/")
def home():
    return {
        "message": "FastAPI + JWT + Curl CRUD"
    }

@app.post("/login")
def login(user: Login):

    if user.username != "admin" or user.password != "admin123":
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        data={"sub": user.username}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": "5 minutes"
    }

@app.post("/todos")
def create_todo(
    todo: Todo,
    user: str = Depends(verify_token)
):

    for existing in todos:
        if existing.id == todo.id:
            raise HTTPException(
                status_code=400,
                detail="ID already exists"
            )

    todos.append(todo)

    return {
        "message": "Todo created",
        "data": todo
    }

@app.get("/todos")
def get_all_todos(
    user: str = Depends(verify_token)
):

    return {
        "count": len(todos),
        "data": todos
    }

@app.get("/todos/{todo_id}")
def get_todo(
    todo_id: int,
    user: str = Depends(verify_token)
):

    for todo in todos:
        if todo.id == todo_id:
            return todo

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )

@app.put("/todos/{todo_id}")
def update_todo(
    todo_id: int,
    updated: Todo,
    user: str = Depends(verify_token)
):

    for index, todo in enumerate(todos):
        if todo.id == todo_id:

            todos[index] = updated

            return {
                "message": "Todo updated successfully",
                "data": updated
            }

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )

@app.delete("/todos/{todo_id}")
def delete_todo(
    todo_id: int,
    user: str = Depends(verify_token)
):

    for index, todo in enumerate(todos):
        if todo.id == todo_id:

            deleted = todos.pop(index)

            return {
                "message": "Todo deleted successfully",
                "data": deleted
            }

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )