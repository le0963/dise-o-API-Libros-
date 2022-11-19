from fastapi import APIRouter
from app.schemas import User,Userid
from uuid import UUID

router = APIRouter(
        prefix="/user",
        tags=["users"] 
)

usuarios = [] 

@router.get('/')
def obtener_usuarios():
    return usuarios

@router.post('/')
def crear_usuario(user:User):
    usuario = user.dict()
    usuarios.append(usuario) 
    print(usuarios) 
    return {"Respuesta":"Usuario creado satisfactoriamente"} 

@router.post('/{user_id }')
def obtener_usuario(user_id:UUID):
    for user in usuarios:
        if user["id"] == user_id:
            return{"usuario":user}
    return{"respuesta":"Usuario no encontrado"} 

@router.post('/obtener_usuario')
def obtener_usuario_2(user_id:Userid): 
    for user in usuarios:
        if user["id"] == user_id.id:
            return{"usuario":user}
    return{"respuesta":"Usuario no encontrado"} 


@router.delete('/{user_id}')
def eliminar_usuario(user_id:UUID):
    for index,user in enumerate(usuarios):
        if user["id"]==user_id:
            usuarios.pop(index)
            return{"Respuesta":"Usuario eliminado correctamente"} 
    return{"respuesta":"usuario no encontrado"} 


@router.put('/{user_id}')
def actualizar_user(user_id:UUID,updateuser:User):
    for index,user in enumerate(usuarios):
        if user["id"]==user_id:
            usuarios[index]["id"] = updateuser.dict()["id"]    
            usuarios[index]["nombre"] = updateuser.dict()["nombre"]    
            usuarios[index]["apellido"] = updateuser.dict()["apellido"]    
            usuarios[index]["direccion"] = updateuser.dict()["direccion"]    
            usuarios[index]["telefono"] = updateuser.dict()["telefono"]    
            return{"Respuesta":"Usuarioactualizado correctamente"} 
    return{"respuesta":"usuario no encontrado"} 

