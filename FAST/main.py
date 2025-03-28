from fastapi import FastAPI
from DB.conexion import engine,Base
from routers.usuarios import routerUsuario
from routers.auth import routerAuth

app = FastAPI(
    title="Mi primer API 194",
    description="Carlos Hernández Méndez",
    version="1.0.1"
)   

Base.metadata.create_all(bind=engine)
 

#EndPoint home
@app.get('/',tags=['Inicio'])
def home():
	return {'hello':'Hello FastAPI!'}

app.include_router(routerUsuario)
app.include_router(routerAuth)