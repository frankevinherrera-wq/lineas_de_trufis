from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Trufi(BaseModel):
    id: int
    linea: str
    color: str
    ruta: str

DATABASE_TRUFIS = [
    {"id": 1, "linea": "102", "color": "Verde", "ruta": "Mercado Central - Terminal"},
    {"id": 2, "linea": "101", "color": "Rojo", "ruta": "Plaza Principal - Aeropuerto"}
]

@app.get("/trufi")
def read_trufis():
    return DATABASE_TRUFIS