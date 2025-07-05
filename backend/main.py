from fastapi import FastAPI, HTTPException
from .inventory import inventory_db, add_item, update_quantity
from .schemas import Item

app = FastAPI(title="SmartInventory API")

@app.get("/")
def root():
    return {"message": "SmartInventory API is running."}

@app.get("/inventory")
def get_inventory():
    return {"inventory": inventory_db}

@app.post("/inventory")
def create_item(item: Item):
    if item.name in inventory_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    add_item(item)
    return {"message": f"Item '{item.name}' added."}

@app.put("/inventory/{item.name}")
def update_item(item_name: str, quantity: int):
    if item_name not in inventory_db:
        raise HTTPException(status_code=404, detail="Item not found")
    update_quantity(item_name, quantity)
    return {"message": f"Quantity for '{item_name}' updated to {quantity}"}

