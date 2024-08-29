from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

# Specifying connection details to the PostgreSQL DB.
DATABASE_URL = "postgresql://postgres:postgres@db:5432/FastAPI_db"

# db:5432 - localhost
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

# Defining Item Model (DB Table)
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Integer, index=True)

Base.metadata.create_all(bind=engine)


class ItemCreate(BaseModel):
    name: str
    description: str = None
    price: float


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Creating a New item Endpoint.
@app.post("/items")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(name=item.name, description=item.description, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Reading all items Endpoint.
@app.get("/items")
def read_items(db: Session = Depends(get_db)):
    return db.query(Item).all()

# Reading a specific item Endpoint.
@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item Not Found!")
    return item
