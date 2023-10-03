from sqlalchemy.orm import Session
import models, schemas
from datetime import datetime

def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todo).offset(skip).limit(limit).all()


def get_todo(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()


def create_todo_item(db: Session, todo: schemas.TodoItemCreate):
    db_todo = models.Todo(title=todo.title, description=todo.description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def update_todo_item(db: Session, todo_id: int, todo: schemas.TodoItemUpdate):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if todo.title is not None:
        db_todo.title = todo.title
    if todo.description is not None:
        db_todo.description = todo.description
    if todo.completed is not None:
        if todo.completed:
            if not db_todo.completed:
                db_todo.completed = True
                db_todo.completed_at = datetime.now()
        else:
            db_todo.completed = False
            db_todo.completed_at = None

    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo_item(db: Session, todo_id: int):
    db_todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    db.delete(db_todo)
    db.commit()
    return db_todo
