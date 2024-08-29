from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

# Specifying connection details to the PostgreSQL DB.
DATABASE_URL = "postgresql://postgres:postgres@db:5432/FastAPI_db"

# db:5432 - localhost
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
