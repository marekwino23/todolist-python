from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import db
from pydantic import BaseModel
from fastapi import status

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TaskRequest(BaseModel):
    name: str

class TaskDeleteRequest(BaseModel):
    id: int    

class TaskResponse(BaseModel):
    id: int
    name: str
    status: bool

class TaskUpdateStatusRequest(BaseModel):
    id: int
    name: str
    status: bool    

@app.route("/")
def home():
    return "<h1>TODO App</h1><p>Użyj /tasks aby zobaczyć zadania</p>"

@app.get("/tasks", response_model=List[TaskResponse], status_code = status.HTTP_200_OK)
def get_tasks():
    tasks = db.get_tasks()  # pobiera listę z db.py
    return tasks   # jsonify robimy dopiero w Flask

@app.post("/tasks", status_code= status.HTTP_201_CREATED)
def add_tasks(task: TaskRequest):
    db.add_task(task.dict())
    return ({"message": "success"}), 201

@app.delete("/delete_tasks", status_code= status.HTTP_200_OK)
def delete_tasks(task: TaskDeleteRequest):
        db.delete_task(task.id)
        return {"message": "success"}

@app.patch("/change_status", status_code= status.HTTP_200_OK)
def change_status_tasks(task: TaskUpdateStatusRequest):
    db.change_status_tasks(task.status, task.id)
    return {"message": "success"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)