from sqlalchemy import Boolean, Column, Integer, String, DateTime, func
from database import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    description = Column(String(200))
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())
    completed_at = Column(DateTime, server_default=None, nullable=True)
