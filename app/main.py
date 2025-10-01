from fastapi import FastAPI
from routes import catequizando

app = FastAPI(
    title= "API Backend Service",
    description="Webservice encargada de guardar y recuperar datos de los alumnos",
    version="1.0.0",
)

# Registrar rutas
app.include_router(catequizando.router, prefix="/catequizando", tags=["Catequizandos"])

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI with Docker!"}

@app.get("/home")
def read_root():
    return {"message": "HOME"}