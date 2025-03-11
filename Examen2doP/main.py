from fastapi import FastAPI, HTTPException
from typing import Optional, List
from models import Vehiculo

app = FastAPI(
    title="App vehiculos",
    description="Reguistro de Vehiculos",
    version="1.0.1"
)

vehiculos=[
	{"año":2000,"Modelo":"porsche", "placa":"1234"},
	{"año":2020,"Modelo":"BMW", "placa":"5678"},
    {"año":2024,"Modelo":"Corvete", "placa":"9101"},
    {"año":2025,"Modelo":"Mustang", "placa":"1213"},
]

@app.get("/vehiculos/", tags=['Operaciones CRUD'])
def leer():
    return vehiculos

@app.post("/vehiculos/",response_model=Vehiculo, tags=['Operaciones CRUD'])
def guardar(vehiculo: Vehiculo):
    for usr in vehiculos:
            if usr["placa"] == vehiculo.placa:
                raise HTTPException(status_code=400, detail="El vehiculo ya existe")
    
    vehiculos.append(vehiculo.dict())
    return vehiculo

@app.delete("/vehiculos/{placa}", tags=['Operaciones CRUD'])
def eliminar(placa: str):
    for vehiculo in vehiculos:
        if vehiculo["placa"] == placa:
            vehiculos.remove(vehiculo)
            return vehiculo
    raise HTTPException(status_code=404, detail="Vehiculo no encontrado")

