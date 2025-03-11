import jwt
from fastapi import HTTPException
from jwt import ExpiredSignatureError, InvalidTokenError 

def createToken(data: dict):
    token: str = jwt.encode(data, 'secretkey', algorithm='HS256') 
    return token

def validateToken(token: str):
    try:
        data: dict = jwt.decode(token, 'secretkey', algorithms=['HS256'])
        return data
    except ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Token Expirado")
    except InvalidTokenError:
        raise HTTPException(status_code=400, detail="Token no Autorizado")
    except Exception:
        raise HTTPException(status_code=400, detail="Token Inválido")
