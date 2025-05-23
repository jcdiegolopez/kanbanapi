from sqlalchemy import Column, Integer, String, DateTime, Enum
from .database import Base
import enum
from datetime import datetime

# Definir los posibles estados y prioridades
class TaskStatus(enum.Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"

class TaskPriority(enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"

# Modelo de la tabla Task
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    status = Column(Enum(TaskStatus), default=TaskStatus.todo)
    priority = Column(Enum(TaskPriority), default=TaskPriority.medium)
    created_at = Column(DateTime, default=datetime.utcnow)