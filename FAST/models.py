from pydantic import BaseModel, Field,EmailStr


class modelUsuario(BaseModel):
    id: int = Field(..., gt=0, description="Id siempre debe ser positivo.")
    nombre: str = Field(..., min_length=1, max_length=85, description="Solo letras y espacios.")
    edad: int = Field(..., gt=0, le=120, description="Edad entre 1 y 120 años.")
    correo: str = Field(..., description="Correo válido.")
    
class modelAuth(BaseModel):
    mail: EmailStr
    passw: str = Field(..., min_length=8, strip_whitespace=True , description="No menos de 8 caracteres sin espacios solo letras")