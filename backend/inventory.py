from .schemas import Item
from .router import router  # ✅ Import FastMCP
import requests

N8N_WEBHOOK_URL = "http://localhost:5678/webhook/low-stock-alert"

# In-memory database
inventory_db = {}

def trigger_low_stock_alert(name, quantity):
    try:
        response = requests.post(N8N_WEBHOOK_URL, json={
            "name": name,
            "quantity": quantity
        })
        response.raise_for_status()
        print(f"n8n alert sent for {name} (Qty: {quantity})")
    except Exception as e:
        print(f"Failed to alert n8n: {e}")

def add_item(item: Item):
    inventory_db[item.name] = {"quantity": item.quantity}

    result = router.route("low-stock-check", {"name": item.name, "quantity": item.quantity})
    print(result["message"])

    if result["trigger_alert"]:
        trigger_low_stock_alert(item.name, item.quantity)

def update_quantity(name: str, quantity: int):
    inventory_db[name]["quantity"] = quantity

    result = router.route("low-stock-check", {"name": name, "quantity": quantity})
    print(result["message"])

    if result["trigger_alert"]:
        trigger_low_stock_alert(name, quantity)
