from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from modelsPydantic import modelUsuario
from middlewares import BearerJWT
from DB.conexion import Session
from models.modelsDB import User
from fastapi import APIRouter

routerUsuario = APIRouter()

@routerUsuario.get('/todosUsuarios',tags=['Operaciones CRUD'])
def leer():
    db=Session()
    try:
        consulta = db.query(User).all()
        return JSONResponse(content=jsonable_encoder(consulta))
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"message":"No fue posible Guardar ",
                                     "Error": str(e)})
    finally:
        db.close()
    
@routerUsuario.get('/usuarios/{id}',tags=['Operaciones CRUD'])
def leeruno(id: int):
    db=Session()
    try:
        consulta = db.query(User).filter(User.id==id).first()
        if not consulta:
            return JSONResponse(status_code=404,
                                content={"message":"Usuario no encontrado"})
        return JSONResponse(content=jsonable_encoder(consulta))
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"message":"No fue posible Guardar ",
                                     "Error": str(e)})
    finally:
        db.close()

#EndPoint para post
@routerUsuario.post('/Usuarios/',response_model=modelUsuario,tags=['Operaciones CRUD'])
def guardar(usuario:modelUsuario):
    db=Session()
    try:
        db.add(User(**usuario.model_dump()))
        db.commit()
        return JSONResponse(status_code=201,
                            content={"message":"Usuario Guardado ",
                                     "usuario": usuario.model_dump()})
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"message":"No fue posible Guardar ",
                                     "Error": str(e)})
        
    finally:
        db.close()

#EndPoint para actualizar
@routerUsuario.put('/Usuarios/{id}', response_model=modelUsuario, tags=['Operaciones CRUD'])
def actualizar(id: int, usuarioActualizado: modelUsuario):
    db = Session()
    try:
        usuario = db.query(User).filter(User.id == id).first()
        if not usuario:
            raise HTTPException(status_code=404, detail="El usuario no existe")
        
        for key, value in usuarioActualizado.model_dump().items():
            setattr(usuario, key, value)
        
        db.commit() 
        return usuarioActualizado.model_dump()  

    except Exception as e:
        db.rollback()  
        return JSONResponse(status_code=500,
                            content={"message": "No fue posible actualizar el usuario",
                                     "Error": str(e)})
    
    finally:
        db.close()  

@routerUsuario.delete('/Usuarios/{id}', tags=['Operaciones CRUD'])
def eliminar(id: int):
    db = Session()
    try:
        
        usuario = db.query(User).filter(User.id == id).first()
        if not usuario:
            raise HTTPException(status_code=404, detail="El usuario no existe")
        
        db.delete(usuario)
        db.commit()  
        return JSONResponse(status_code=200, content={"message": "Usuario eliminado exitosamente"})

    except Exception as e:
        db.rollback()  
        return JSONResponse(status_code=500,
                            content={"message": "No fue posible eliminar el usuario",
                                     "Error": str(e)})
    
    finally:
        db.close()