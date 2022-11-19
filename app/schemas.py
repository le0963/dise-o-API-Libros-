from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID


#User Model
class User(BaseModel):
    id: UUID
    nombre:str
    apellido:str
    direccion:Optional[str]
    telefono:int
    creacion_user:datetime = datetime.now() 

class Userid(BaseModel):
    id: UUID

#Book Model

class Book(BaseModel):
    id: UUID
    titulo:str
    autor:str
    calificacion:Optional[int]
    creacion_user:datetime = datetime.now() 

class Bookid(BaseModel):
    id: UUID
