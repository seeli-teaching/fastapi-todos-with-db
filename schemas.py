from datetime import datetime
from pydantic import BaseModel

class TodoItem(BaseModel):
    id: int
    title: str
    description: str = None
    completed: bool = False
    created_at: datetime = datetime.now()
    completed_at: datetime = None

class TodoItemUpdate(BaseModel):
    title: str = None
    description: str = None
    completed: bool = False
    
class TodoItemCreate(BaseModel):
    title: str
    description: str = None