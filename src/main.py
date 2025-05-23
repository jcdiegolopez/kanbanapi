from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import engine, Base
from .schemes import TaskCreate, TaskUpdate, Task, APIResponse
from .crud import create_task, get_task, get_tasks, update_task, delete_task
from .database import get_db

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Crear la aplicación FastAPI
app = FastAPI(title="Kanban API", description="API para gestionar tareas en un tablero Kanban")

# Crear una tarea
@app.post("/tasks/", response_model=APIResponse)
def create_new_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = create_task(db, task)
    pydantic_task = Task.model_validate(db_task)
    return APIResponse(
        status="success",
        message=f"Tarea creada con éxito con ID {db_task.id}",
        data=pydantic_task.model_dump()
    )

# Obtener una tarea por ID
@app.get("/tasks/{task_id}", response_model=APIResponse)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = get_task(db, task_id)
    if db_task is None:
        raise HTTPException(
            status_code=404,
            detail=APIResponse(
                status="error",
                message=f"Tarea con ID {task_id} no encontrada",
                data=None
            ).model_dump()
        )
    pydantic_task = Task.model_validate(db_task)
    return APIResponse(
        status="success",
        message=f"Tarea con ID {task_id} obtenida con éxito",
        data=pydantic_task.model_dump()
    )

# Listar todas las tareas
@app.get("/tasks/", response_model=APIResponse)
def read_tasks(db: Session = Depends(get_db)):
    tasks = get_tasks(db)
    pydantic_tasks = [Task.model_validate(task) for task in tasks]
    return APIResponse(
        status="success",
        message=f"{len(tasks)} tareas obtenidas con éxito",
        data=[task.model_dump() for task in pydantic_tasks]
    )

# Actualizar una tarea
@app.put("/tasks/{task_id}", response_model=APIResponse)
def update_existing_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    db_task = update_task(db, task_id, task)
    if db_task is None:
        raise HTTPException(
            status_code=404,
            detail=APIResponse(
                status="error",
                message=f"Tarea con ID {task_id} no encontrada",
                data=None
            ).model_dump()
        )
    pydantic_task = Task.model_validate(db_task)
    return APIResponse(
        status="success",
        message=f"Tarea con ID {task_id} actualizada con éxito",
        data=pydantic_task.model_dump()
    )

# Eliminar una tarea
@app.delete("/tasks/{task_id}", response_model=APIResponse)
def delete_existing_task(task_id: int, db: Session = Depends(get_db)):
    db_task = delete_task(db, task_id)
    if db_task is None:
        raise HTTPException(
            status_code=404,
            detail=APIResponse(
                status="error",
                message=f"Tarea con ID {task_id} no encontrada",
                data=None
            ).model_dump()
        )
    pydantic_task = Task.model_validate(db_task)
    return APIResponse(
        status="success",
        message=f"Tarea con ID {task_id} eliminada con éxito",
        data=pydantic_task.model_dump()
    )