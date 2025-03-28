from fastapi.responses import JSONResponse
from modelsPydantic import modelAuth
from gentoken import createToken
from fastapi import APIRouter

routerAuth = APIRouter()

#EndPoint para generar Token
@routerAuth.post('/auth',tags=['autentificacion'])
def auth(credenciales: modelAuth):
    if credenciales.mail == 'carlos@example.com' and credenciales.passw == '123456789':
        token: str= createToken(credenciales.model_dump())
        print(token)
        return JSONResponse(content={"token": token})
    else:
        return {"Aviso": "Usuario no cuenta con permisos"}