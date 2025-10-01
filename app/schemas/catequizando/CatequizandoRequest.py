
from pydantic import BaseModel
from typing import Union

class CatequizandoRequest(BaseModel):
    nombre: str
    edad: int
    email: Union[str, None]