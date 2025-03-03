import jwt
from fastapi import HTTPException
from jwt import ExpiredSignatureError, InvalidTokenError 

def createToken(data: dict):
    # Crear el token con la clave secreta
    token: str = jwt.encode(data, 'secretkey', algorithm='HS256')  # Asegúrate de que sea compatible con tu versión de PyJWT
    return token

def validateToken(token: str):
    try:
        # Decodificar el token, validando la firma
        data: dict = jwt.decode(token, 'secretkey', algorithms=['HS256'], options={"verify_signature": True})
        return data
    except ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Token Expirado")
    except InvalidTokenError:
        raise HTTPException(status_code=400, detail="Token no Autorizado")
    except Exception:
        raise HTTPException(status_code=400, detail="Token Inválido")
