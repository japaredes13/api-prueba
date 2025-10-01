from fastapi import APIRouter
from schemas.catequizando.CatequizandoResponse import CatequizandoResponse
from schemas.catequizando.CatequizandoRequest import CatequizandoRequest

router = APIRouter()

catequizando_list = [
    CatequizandoResponse(
        id=1,
        nombre="Javier",
        apellido="Hernández",
        edad=20,
        telefono="123456789",
        email="javier@gmail.com",
        fecha_nacimiento="1990-01-01",
    ),
    CatequizandoResponse(
        id=2,
        nombre="Pepe",
        apellido="Perez",
        edad=21,
        telefono="987654321",
        email="pepe@gmail.com",
        fecha_nacimiento="1990-02-02",
    ),
]

@router.get(
    "/",
    response_model=list[CatequizandoResponse],
    status_code=200,
)
def listar_catequizando():
    return catequizando_list


@router.get(
    "/{id}",
    response_model=CatequizandoResponse,
    status_code=200,
)
def get_catequizando(id: int):
    for catequizando in catequizando_list:
        if catequizando.id == id:
            return catequizando
    raise ValueError(f"No se encontró el alumno con id {id}")


@router.put(
    "/{id}",
    response_model=CatequizandoResponse,
    status_code=200,
)
def update_catequizando(id: int, catequizandoUpdate: CatequizandoRequest):
    for catequizando in catequizando_list:
        if catequizando.id == id:
            catequizando.nombre = catequizandoUpdate.nombre
            catequizando.edad = catequizandoUpdate.edad
            catequizando.email = catequizandoUpdate.email
            return catequizando
    raise ValueError(f"No se encontró el alumno con id {id}")