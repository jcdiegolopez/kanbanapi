from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexión a PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost/kanban_db"

# Crear el motor de SQLAlchemy (conecta con la base de datos)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear una fábrica de sesiones para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para definir los modelos de la base de datos
Base = declarative_base()

# Dependencia para obtener una sesión de base de datos en los endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()