from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()

FILE_PATH = "tasks.json"


class Task(BaseModel):
    title: str
    status: str


class TaskStatus(BaseModel):
    status: str


if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w") as file:
        json.dump([], file)


@app.get("/")
def home():
    return {"message": "TODO API is working"}


@app.get("/tasks")
def get_tasks():

    with open(FILE_PATH, "r") as file:
        tasks = json.load(file)

    return tasks


@app.post("/tasks")
def create_task(task: Task):

    with open(FILE_PATH, "r") as file:
        tasks = json.load(file)

    new_id = max([item["id"] for item in tasks], default=0) + 1

    new_task = {
        "id": new_id,
        "title": task.title,
        "status": task.status
    }

    tasks.append(new_task)

    with open(FILE_PATH, "w") as file:
        json.dump(tasks, file, indent=4)

    return new_task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, data: TaskStatus):

    with open(FILE_PATH, "r") as file:
        tasks = json.load(file)

    for task in tasks:

        if task["id"] == task_id:

            task["status"] = data.status

            with open(FILE_PATH, "w") as file:
                json.dump(tasks, file, indent=4)

            return task

    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    with open(FILE_PATH, "r") as file:
        tasks = json.load(file)

    for task in tasks:

        if task["id"] == task_id:

            tasks.remove(task)

            with open(FILE_PATH, "w") as file:
                json.dump(tasks, file, indent=4)

            return {"message": "Task deleted successfully"}

    raise HTTPException(status_code=404, detail="Task not found")