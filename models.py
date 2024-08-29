from sqlalchemy import create_engine, Column, Integer, String, Float
from database import Base


# Defining Item Model (DB Table)
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Integer, index=True)
