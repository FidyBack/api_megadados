from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Food(BaseModel):
    name: str
    quantity: int
    bought: bool

database={
    1:Food(name= "pasta", quantity=50, bought=1),
    2:Food(name= "pineaple", quantity=100, bought=0)
}

@app.get("/items")
def read_root():
    
    return database

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if (item_id in database):
        return database[item_id]
    else:
        pass

@app.get("/items/bought/{paid}")
def read_bought_item(paid: bool):
    data={}
    for i in database:
        if (database[i].bought==paid):
            data[i]=database[i]
            return data
    
@app.post("/items/add/{item_id}")
def update_item(item_id: int, item: Food):
    if not(item_id in database):
        database[item_id]= item
    else:
        pass

@app.put("/items/update/{item_id}")
def update_item(item_id: int, amount: int):
    if (item_id in database):
        database[item_id].quantity = amount
    else:
        pass

@app.put("items/bought/{item_id}")
def bought_item(item_id: int, paid: bool):
    if (item_id in database):
        database[item_id].bought = paid
    else:
        pass

@app.delete("/items/delete/{item_id}")
def delete_item(item_id:int):
    if (item_id in database):
        del database[item_id]
        return ("deletion ")
    else:
        pass



