from pydantic import BaseModel
from typing import Union

class CatequizandoResponse(BaseModel):
    id: int
    nombre: str
    apellido: str
    edad: int
    telefono: Union[str, None]
    email: Union[str, None]
    fecha_nacimiento: str
