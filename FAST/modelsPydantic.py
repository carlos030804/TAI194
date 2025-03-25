from pydantic import BaseModel, Field,EmailStr


class modelUsuario(BaseModel):
    name: str = Field(..., min_length=1, max_length=85, description="Solo letras y espacios.")
    age: int 
    email: str 
    
class modelAuth(BaseModel):
    mail: EmailStr
    passw: str = Field(..., min_length=8, strip_whitespace=True , description="No menos de 8 caracteres sin espacios solo letras")