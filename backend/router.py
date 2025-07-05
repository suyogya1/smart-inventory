from typing import Dict

# Simulate a lightweight FastMCP-style router
class FastMCP:
    def __init__(self):
        self.tasks = {}

    def task(self, name):
        def decorator(func):
            self.tasks[name] = func
            return func
        return decorator

    def route(self, task_name, data):
        task = self.tasks.get(task_name)
        if task:
            return task(data)
        else:
            raise ValueError(f"Task '{task_name}' not registered in router.")

# Create router instance
router = FastMCP()

# Define a routing rule for low stock check
@router.task("low-stock-check")
def handle_low_stock(data: Dict):
    quantity = data.get("quantity", 0)
    name = data.get("name", "Unknown Item")

    if quantity < 3:
        return {
            "action": "critical",
            "message": f"{name} is critically low (only {quantity} left).",
            "trigger_alert": True
        }
    elif quantity < 10:
        return {
            "action": "low",
            "message": f"{name} is low in stock ({quantity}).",
            "trigger_alert": True
        }
    else:
        return {
            "action": "safe",
            "message": f"{name} has sufficient stock.",
            "trigger_alert": False
        }
