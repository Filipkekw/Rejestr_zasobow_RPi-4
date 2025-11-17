#!/usr/bin/env python3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
from logic.db import Database
from logic.export import export_inventory_to_csv
import uvicorn

app = FastAPI(title="Inventory WiFi Server")

# --- inicjalizacja bazy ---
data_dir = Path(__file__).resolve().parent / "data"
data_dir.mkdir(exist_ok=True)
db = Database(data_dir / "inventory.db")

# --- modele danych ---
class Item(BaseModel):
    id: int | None = None
    name: str
    category: str
    purchase_date: str
    serial_number: str
    description: str


# --- endpointy API ---
@app.get("/items")
def list_items():
    return db.list_items()

@app.post("/items")
def add_item(item: Item):
    new_id = db.add_item(**item.dict(exclude={"id"}))
    return {"status": "ok", "id": new_id}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    db.update_item(item_id, **item.dict(exclude={"id"}))
    return {"status": "ok"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    db.delete_item(item_id)
    return {"status": "ok"}

@app.get("/export")
def export_csv():
    path = data_dir / "export.csv"
    export_inventory_to_csv(db.list_items(), path)
    return {"status": "ok", "path": str(path)}

@app.get("/ping")
def ping():
    return {"status": "ok", "message": "pong"}


# --- startowanie serwera ---
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)