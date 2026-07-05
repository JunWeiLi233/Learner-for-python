from fastapi import FastAPI, HTTPException
from typing import List, Optional
from pydantic import BaseModel, Field
from enum import IntEnum

api = FastAPI()

class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1

class TodoBase(BaseModel):
    todo_name: str = Field(..., min_length = 3, max_length=512, description="Name of the todo")
    todo_description: str = Field(..., description="description of the todo")
    priority: Priority = Field(default=Priority.LOW, description="Priority of the todo")

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    todo_id: int = Field(..., description = "Unique identifier of the todo")

class TodoUpdate(BaseModel):
    todo_name: Optional[str] = Field(None, min_length = 3, max_length=512, description="Name of the todo")
    todo_description: Optional[str] = Field(None, description="description of the todo")
    priority: Optional[Priority] = Field(None, description="Priority of the todo")

all_todos =[
    Todo(todo_id=1, todo_name="sports", todo_description="go to the gym", priority = Priority.HIGH),
    Todo(todo_id=2, todo_name="read", todo_description="read 10 pages", priority = Priority.MEDIUM),
    Todo(todo_id=3, todo_name="shop", todo_description="go shopping", priority = Priority.LOW),
    Todo(todo_id=4, todo_name="study", todo_description="study for exam", priority = Priority.MEDIUM),
    Todo(todo_id=5, todo_name="meditate", todo_description="meditate 20 minutes", priority = Priority.LOW),
]
# GET: Get information from server
# POST: Create information for server
# PUT: Change information for server
# DELETE: Delete information from server

@api.get("/todos/{todo_id}", response_model = Todo)
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail='Todo not found')
        
@api.get("/todos", response_model=List[Todo])
def get_todo(first_n: int = None):
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos
    
@api.post('/todos', response_model=Todo)
def create_todo(todo: TodoCreate):
    new_todo_id = max(t.todo_id for t in all_todos) + 1
    new_todo = Todo(todo_id = new_todo_id, 
                    todo_name = todo.todo_name, 
                    todo_description = todo.todo_description,
                    priority = todo.priority)

    all_todos.append(new_todo)
    return new_todo

@api.put('/todos/{todo_id}', response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoUpdate):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            if updated_todo.todo_name is not None:
                todo.todo_name = updated_todo.todo_name
            if updated_todo.todo_description is not None:
                todo.todo_description = updated_todo.todo_description
            if updated_todo.priority is not None:
                todo.priority = updated_todo.priority
            return todo
    raise HTTPException(status_code=404, detail='Todo not found')

@api.delete('/todos/{todo_id}', response_model=Todo)
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo.todo_id == todo_id:
            delete_todo = all_todos.pop(index)
            return delete_todo
    raise HTTPException(status_code=404, detail='Todo not found')