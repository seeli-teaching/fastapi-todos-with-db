from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException
from schemas import TodoItemUpdate, TodoItemCreate
from database import SessionLocal, engine
import repository
import models

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get("/")
def index():
    return {"Hello": "FastAPI"}


# Get all todos
@app.get("/todos")
def get_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = repository.get_todos(db, skip=skip, limit=limit)
    return todos


# Get one todo
@app.get("/todos/{todo_id}")
def get_one_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = repository.get_todo(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(
            status_code=404, detail=f"Todo with id {todo_id} not found")
    return db_todo


# Create a todo
@app.post("/todos")
def create_todo(todo: TodoItemCreate, db: Session = Depends(get_db)):
    return repository.create_todo_item(db=db, todo=todo)


# Update a todo
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo: TodoItemUpdate, db: Session = Depends(get_db)):
    db_todo = repository.get_todo(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(
            status_code=404, detail=f"Todo with id {todo_id} not found")

    return repository.update_todo_item(db=db, todo_id=todo_id, todo=todo)


# Delete a todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = repository.get_todo(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(
            status_code=404, detail=f"Todo with id {todo_id} not found")
    repository.delete_todo_item(db=db, todo_id=todo_id)
    return {"Message": f"Todo with id {todo_id} successfully deleted"}
