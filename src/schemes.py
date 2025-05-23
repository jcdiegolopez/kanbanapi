from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional, Any, Dict, List
from .models import TaskStatus, TaskPriority

# Esquema base para Task
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.todo
    priority: TaskPriority = TaskPriority.medium

# Esquema para crear una tarea
class TaskCreate(TaskBase):
    pass

# Esquema para actualizar una tarea
class TaskUpdate(TaskBase):
    pass

# Esquema para leer una tarea (incluye id y created_at)
class Task(TaskBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

# Esquema para respuestas estándar de la API
class APIResponse(BaseModel):
    status: str
    message: str
    data: Optional[List[Any] | Dict[str, Any]] = None