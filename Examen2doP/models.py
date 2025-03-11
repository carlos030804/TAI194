import pydantic as pydantic
from pydantic import BaseModel, Field

class Vehiculo (BaseModel):
    año: int = Field(...,min_lenght=5, description="solo tiene que tener 4 digitos")
    modelo: str = Field(...,max_lenght=25, description="Maximo 25 caracteres")
    placa: str= Field(...,max_lenght=10, description="Maximo 10 caracteres")
    

    