from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from typing import Optional, List
from models import modelUsuario, modelAuth
from gentoken import createToken
from middlewares import BearerJWT

app = FastAPI(
    title="Mi primer API",
    description="Carlos Hernández Méndez",
    version="1.0.1"
)    
usuarios=[
	{"id":1,"nombre":"carlos", "edad":20, "correo":"carlos@example.com"},
	{"id":2,"nombre":"Paulina", "edad":24, "correo":"122041771@upq.edu.mx"},
	{"id":3,"nombre":"Saul", "edad":21, "correo":"122041772@upq.edu.mx"},
	{"id":4,"nombre":"Maye", "edad":26, "correo":"122041773@upq.edu.mx"},
	{"id":5,"nombre":"Yasmin", "edad":42, "correo":"122041774@upq.edu.mx"},
]

#EndPoint home
@app.get('/',tags=['Inicio'])
def home():
	return {'hello':'Hello FastAPI!'}

#EndPoint para generar Token
@app.post('/auth',tags=['autentificacion'])
def auth(credenciales: modelAuth):
    if credenciales.mail == 'carlos@example.com' and credenciales.passw == '123456789':
        token: str= createToken(credenciales.model_dump())
        print(token)
        return JSONResponse(content={"token": token})
    else:
        return {"Aviso": "Usuario no cuenta con permisos"}


#EndPoint CONSULTA TODOS
@app.get('/todosUsuarios', dependencies=[Depends(BearerJWT())], response_model=List[modelUsuario], tags=['Operaciones CRUD'])
def leer():
	return usuarios

#EndPoint para post
@app.post('/Usuarios/',response_model=modelUsuario,tags=['Operaciones CRUD'])
def guardar(usuario:modelUsuario):
    for usr in usuarios:
            if usr ["id"] == usuario.id:
                raise  HTTPException(status_code=400,detail="El usuario ya existe")
    
    usuarios.append(usuario)
    return usuario 

#EndPoint para actualizar
@app.put('/Usuarios/{id}',response_model=modelUsuario,tags=['Operaciones CRUD'])
def actualizar(id:int,usuarioActualizado:modelUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios[index]=usuarioActualizado.model_dump()
            return usuarios[index]
    
    raise HTTPException(status_code=400,detail="El usuario no existe")

@app.delete('/Usuarios/{id}',tags=['Operaciones CRUD'])
def eliminar(id:int):
    for index, usr in enumerate(usuarios):
        if usr["id"] == id:
            usuarios.pop(index)
            return usuarios[index]
    
    raise HTTPException(status_code=400,detail="El usuario no existe")