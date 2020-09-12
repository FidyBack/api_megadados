from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Food(BaseModel):
    name: str
    quantity: int
    bought: bool = False

database={
    1:Food(name= "pasta", quantity=50, bought=1),
    2:Food(name= "pineaple", quantity=100, bought=0)
}

@app.get("/items")
def read_root():
    """
    Return all itens
    """
    return database


@app.get("/items/{item_id}")
def read_item(item_id: int):
    """
    Return an specific item from the database
    """
    if (item_id in database):
        return database[item_id]
    else:
        raise HTTPException(status_code = 404, detail = "Item Not Found")


@app.get("/items/bought/{paid}")
def read_bought_item(paid: bool):
    """
    Return itens with status 'bouht = True'
    """
    data={}
    for i in database:
        if (database[i].bought==paid):
            data[i]=database[i]
            return data


@app.post("/items/add/{item_id}")
def add_item(item_id: int, item: Food):
    """
    Create new itens in the database
    """
    if not(item_id in database):
        database[item_id] = item
        raise HTTPException(status_code = 201, detail = "Item created succesfully")
    else:
        raise HTTPException(status_code = 409, detail = "ID already exist")


@app.put("/items/update/{item_id}")
def update_item(item_id: int, amount: int):
    """
    Update item in the database
    """
    if (item_id in database):
        database[item_id].quantity = amount
        raise HTTPException(status_code = 200, detail = "Item updated succesfully")
    else:
        raise HTTPException(status_code = 404, detail = "Item Not Found")


@app.put("items/buy/{item_id}")
def buy_item(item_id: int):
    """
    Update item from unpaid to paid
    """
    if (item_id in database):
        database[item_id].bought = True
        raise HTTPException(status_code = 200, detail = "Item bought succesfully")
    else:
        raise HTTPException(status_code = 404, detail = "Item Not Found")


@app.delete("/items/delete/{item_id}")
def delete_item(item_id:int):
    if (item_id in database):
        del database[item_id]
        raise HTTPException(status_code = 200, detail = "Item removed succesfully")
    else:
        raise HTTPException(status_code = 404, detail = "Item Not Found")