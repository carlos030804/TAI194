from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title="Mi primer API",
    description="Carlos Hernández Méndez",
    version="1.0.1"
)

usuarios=[
	{"id":1,"nombre":"carlos", "edad":20},
	{"id":2,"nombre":"Paulina", "edad":24},
	{"id":3,"nombre":"Saul", "edad":21},
	{"id":4,"nombre":"Maye", "edad":26},
	{"id":5,"nombre":"Yasmin", "edad":42},
]

#EndPoint home
@app.get('/',tags=['Inicio'])
def home():
	return {'hello':'Hello FastAPI!'}

#EndPoint Consulta todos
@app.get('/todosusuarios',tags=['Operaciones CRUD'])
def leer():
	return {'Usuarios Rguistrados':usuarios}

#EndPoint para post
@app.post('/Usuarios/',tags=['Operaciones CRUD'])
def guardar(usuario:dict):
    for usr in usuarios:
            if usr ["id"] == usuario.get("id"):
                raise  HTTPException(status_code=400,detail="El usuario ya existe")
    
    usuarios.append(usuario)
    return usuario 

#EndPoint para actualizar
@app.put('/Usuarios/{id}',tags=['Operaciones CRUD'])
def actualizar(id:int,usuarioActualizado:dict):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index].update(usuarioActualizado)
            return usuarios[index]
    
    raise HTTPException(status_code=400,detail="El usuario no existe")

@app.delete('/Usuarios/{id}',tags=['Operaciones CRUD'])
def eliminar(id:int):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios.pop(index)
            return usuarios[index]
    
    raise HTTPException(status_code=400,detail="El usuario no existe")