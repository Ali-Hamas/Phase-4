from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import os

app = FastAPI(title="Todo Chatbot API", version="1.0.0")

# Models
class TodoItem(BaseModel):
    id: Optional[int] = None
    title: str
    completed: bool = False

class TodoResponse(BaseModel):
    id: int
    title: str
    completed: bool

# In-memory storage (would be replaced with database in production)
todos_db: List[TodoResponse] = []
next_id = 1

@app.get("/")
def read_root():
    return {"message": "Todo Chatbot API is running!"}

@app.get("/todos", response_model=List[TodoResponse])
def get_todos():
    return todos_db

@app.post("/todos", response_model=TodoResponse)
def create_todo(todo: TodoItem):
    global next_id
    new_todo = TodoResponse(id=next_id, title=todo.title, completed=todo.completed)
    todos_db.append(new_todo)
    next_id += 1
    return new_todo

@app.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, todo: TodoItem):
    for i, existing_todo in enumerate(todos_db):
        if existing_todo.id == todo_id:
            updated_todo = TodoResponse(id=todo_id, title=todo.title, completed=todo.completed)
            todos_db[i] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    global todos_db
    initial_length = len(todos_db)
    todos_db = [todo for todo in todos_db if todo.id != todo_id]
    if len(todos_db) == initial_length:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}

@app.delete("/todos")
def delete_all_todos():
    global todos_db
    todos_db.clear()
    return {"message": "All todos deleted successfully"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)