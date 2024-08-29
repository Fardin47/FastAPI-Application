from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()


models.Base.metadata.create_all(bind=engine)


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
    db_item = models.Item(
        name=item.name, description=item.description, price=item.price
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Reading all items Endpoint.
@app.get("/items")
def read_items(db: Session = Depends(get_db)):
    return db.query(models.Item).all()

# Reading a specific item Endpoint.
@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item Not Found!")
    return item
