from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


items = []

class Item(BaseModel):
    name: str
    description: str = None
    price: float

@app.get("/items", description="This route is to return list of items")
def read_items():
    return items


@app.post("/items", description="This route is to create an item")
def create_item(item: Item):
    item_id = len(items) + 1
    item_dict = item.model_dump()
    item_dict.update({"id": item_id})
    items.append(item_dict)
    return item_dict


@app.get("/items/{item_id}", description="This route is to return a specific item")
def read_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
