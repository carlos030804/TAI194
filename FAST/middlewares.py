from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer
from gentoken import validateToken

class BearerJWT(HTTPBearer):
    async def _call_(self, request: Request):
        auth = await super()._call_(request)

        data = validateToken(auth.credentials)

        if not isinstance(data, dict): 
            raise HTTPException(status_code=401, detail="Token Inválido")

        if data.get('email') != 'carlos@example.com':
            raise HTTPException(status_code=403, detail="Credenciales no válidas")