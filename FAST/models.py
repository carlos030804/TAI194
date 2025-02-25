from pydantic import BaseModel,Field

class modelUsuario(BaseModel):
    id: int =Field(...,gt=0, description="ID siempre debe ser positivo")
    nombre: str =Field(...,min_lenth= 1, max_length=85 , description="Solo letras y espacios min 1 y max 85 ")
    edad: int =Field (...,gt= 0, Ie=120 , description="La edad siempre debe ser positiva min 1 max 120")
    correo: str = Field(..., Regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", Example="correo@domain")