# Kanban API

## Descripción
Kanban API es una aplicación backend desarrollada para gestionar tareas en un tablero Kanban. La API permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre tareas, así como listar todas las tareas disponibles. Está construida con **FastAPI**, utiliza **PostgreSQL** como base de datos y **SQLAlchemy** como ORM para interactuar con la base de datos. Los esquemas de validación están implementados con **Pydantic**, y las respuestas de la API están estandarizadas para facilitar la integración con el frontend.

## Tecnologías utilizadas
- **Python 3.9+**: Lenguaje principal.
- **FastAPI**: Framework para crear la API, elegido por su rapidez, validación automática y documentación automática (Swagger).
- **SQLAlchemy**: ORM para gestionar la base de datos relacional.
- **PostgreSQL**: Base de datos relacional para almacenar las tareas.
- **Pydantic**: Validación de datos de entrada y salida.
- **Uvicorn**: Servidor ASGI para ejecutar la aplicación.
- **Postman**: Herramienta para probar los endpoints de la API.

## Estructura del proyecto
```
kanban-api/
├── .gitignore              
├── README.md               
├── requirements.txt        # Dependencias del proyecto
├── Kanban api.postman_collection.json # Colección de Postman para probar los endpoints
├── src/
│   ├── __init__.py         
│   ├── main.py             # endpoints de la API
│   ├── database.py         # Configuración de la base de datos
│   ├── models.py           # Modelos de la base de datos (tabla tasks)
│   ├── schemas.py          # Esquemas Pydantic para validación
│   ├── crud.py             # Operaciones CRUD
```

## Requisitos previos
1. **Python 3.9+**: Instala Python desde [python.org](https://www.python.org/downloads/).
2. **PostgreSQL**: Instala PostgreSQL (versión 13 o superior) localmente o usa un contenedor Docker.
3. **Git**: Para clonar el repositorio.
4. **Postman**: Para probar los endpoints con la colección proporcionada.

## Instalación
1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/jcdiegolopez/kanbanapi
   cd kanbanapi
   ```

2. **Crea y activa un entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura la base de datos PostgreSQL**:
   - Crea una base de datos llamada `kanban_db`:
     ```sql
     CREATE DATABASE kanban_db;
     ```
   - Actualiza la URL de conexión en `src/database.py` si es necesario:
     ```python
     SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost/kanban_db"
     ```
     Cambia `postgres:password` por tus credenciales de PostgreSQL.

5. **Ejecuta la aplicación**:
   ```bash
   uvicorn src.main:app --reload
   ```
   - La API estará disponible en `http://localhost:8000`.
   - Accede a la documentación interactiva en `http://localhost:8000/docs`.

## Configuración de la base de datos
- La aplicación crea automáticamente la tabla `tasks` al iniciarse, gracias a `Base.metadata.create_all` en `main.py`.
- Asegúrate de que PostgreSQL esté corriendo y que la base de datos `kanban_db` exista antes de ejecutar la aplicación.

## Uso de la API
La API proporciona los siguientes endpoints para gestionar tareas en un tablero Kanban:

| Método | Endpoint             | Descripción                              |
|--------|----------------------|------------------------------------------|
| GET    | `/tasks/`            | Lista todas las tareas                   |
| POST   | `/tasks/`            | Crea una nueva tarea                     |
| GET    | `/tasks/{task_id}`   | Obtiene una tarea por ID                 |
| PUT    | `/tasks/{task_id}`   | Actualiza una tarea existente            |
| DELETE | `/tasks/{task_id}`   | Elimina una tarea por ID                 |

### Ejemplo de solicitud (POST /tasks/)
```json
{
    "title": "Tarea de prueba",
    "description": "Descripción opcional",
    "status": "todo",
    "priority": "medium"
}
```

### Respuesta estandarizada
Todas las respuestas siguen el formato:
```json
{
    "status": "success",
    "message": "Operación realizada con éxito",
    "data": {...}
}
```

## Probar con Postman
1. Importa la colección `Kanban api.postman_collection.json` en Postman.
2. Configura la variable `base_url` en Postman con el valor `http://localhost:8000`.
3. Usa los endpoints de la colección para probar las operaciones CRUD:
   - **Get All tasks**: Lista todas las tareas.
   - **Create task**: Crea una nueva tarea.
   - **Get task by id**: Obtiene una tarea específica.
   - **Update task by id**: Actualiza una tarea.
   - **Delete task by id**: Elimina una tarea.

## Notas
- La colección de Postman incluye ejemplos de solicitudes para cada endpoint, con cuerpos JSON preconfigurados para crear y actualizar tareas.
- La API valida los datos de entrada usando Pydantic, asegurando que los campos `status` y `priority` solo acepten valores válidos (`todo`, `in_progress`, `done` para `status`; `low`, `medium`, `high` para `priority`).




