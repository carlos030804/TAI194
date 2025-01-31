from fastapi import FastAPI
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

#EndPoint promedio
@app.get('/promedio',tags=['Mi calificación TAI'])
def promedio():
	return 10.5

#EndPoint parámetro obligatorio
@app.get('/usuario/{id}',tags=['Endpoint Parámetro Obligatorio'])
def consultausuario(id:int):
	#Caso ficticio de busqueda en BD
	return {"Se encontró el usuario":id}

#EndPoint parámetro opcional
#No lleva el parámetro en las llaves
@app.get('/usuario2/',tags=['Endpoint Parámetro Opcional'])
def consultausuario2(id: Optional[int]=None):
    if id is not None:
        for usuario in usuarios:
            if usuario  ["id"] == id:
                return {"mensaje":"usuario encontrado", "El usuario es:":usuario}
            return {"mensaje":f"No se encontraro el id {id}"}

        return {"mensaje":"No se proporciono un id"}


#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
        usuario_id: Optional[int] = None,
        nombre: Optional[str] = None,
        edad: Optional[int] = None
    ):
        resultados = []

        for usuario in usuarios:
            if (
                (usuario_id is None or usuario["id"] == usuario_id) and
                (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
                (edad is None or usuario["edad"] == edad)
            ):
                resultados.append(usuario)

        if resultados:
            return {"usuarios_encontrados": resultados}
        else:
            return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}