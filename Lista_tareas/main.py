from fastapi import FastAPI, HTTPException
from typing import Optional
from datetime import date

app = FastAPI(
    title="API_Tareas",
    description="API para gestionar tareas",
    version="1.0.1"
)

tareas = [
    {"id": 1, "titulo": "tarea_1", "descripcion": "hacer un resumen", "vencimiento": "2025-02-17", "estado": "activo"},
    {"id": 2, "titulo": "tarea_2", "descripcion": "investigar", "vencimiento": "2025-03-10", "estado": "activo"},
    {"id": 3, "titulo": "tarea_3", "descripcion": "leer un libro", "vencimiento": "2025-04-05", "estado": "activo"},
    {"id": 4, "titulo": "tarea_4", "descripcion": "hacer ejercicio", "vencimiento": "2025-05-01", "estado": "activo"},
    {"id": 5, "titulo": "tarea_5", "descripcion": "practicar código", "vencimiento": "2025-06-20", "estado": "activo"},
]

# EndPoint home
@app.get('/', tags=['Inicio'])
def home():
    """Endpoint de bienvenida a la API."""
    return {"hello": "Hello FastAPI!"}

# EndPoint consulta todas las tareas
@app.get("/tareas", tags=['Operaciones CRUD'])
def obtener_tareas():
    """Devuelve la lista de todas las tareas registradas."""
    return tareas

# EndPoint para consultar una tarea por su ID
@app.get("/tareas/{tarea_id}", tags=['Operaciones CRUD'])
def obtener_tarea(tarea_id: int):
    """Obtiene los detalles de una tarea específica."""
    for tarea in tareas:
        if tarea["id"] == tarea_id:
            return tarea
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

# EndPoint para crear tareas
@app.post("/tareas", tags=['Operaciones CRUD'])
def crear_tarea(tarea: dict):
    """Guarda una nueva tarea. No debe existir previamente."""
    for t in tareas:
        if t["id"] == tarea["id"]:
            raise HTTPException(status_code=400, detail="El ID ya existe")
    tareas.append(tarea)
    return tarea

# EndPoint para actualizar
@app.put("/tareas/{tarea_id}", tags=['Operaciones CRUD'])
def actualizar_tarea(tarea_id: int, tarea_actualizada: dict):
    """Actualiza los datos de una tarea existente por su ID."""
    for index, tarea in enumerate(tareas):
        if tarea["id"] == tarea_id:
            tareas[index].update(tarea_actualizada)
            return tareas[index]
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

# EndPoint para eliminar
@app.delete("/tareas/{tarea_id}", tags=['Operaciones CRUD'])
def eliminar_tarea(tarea_id: int):
    """Elimina una tarea existente por su ID."""
    for index, tarea in enumerate(tareas):
        if tarea["id"] == tarea_id:
            return tareas.pop(index)
    raise HTTPException(status_code=404, detail="Tarea no encontrada")