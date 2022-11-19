from fastapi import APIRouter
from app.schemas import Book,Bookid
from uuid import UUID

router = APIRouter(
        prefix="/libro",
        tags=["libros"] 
)

libros = [] 

@router.get('/')
def obtener_libros():
    return libros

@router.post('/')
def crear_libro(book:Book):
    libro = book.dict()
    libros.append(libro) 
    print(libros) 
    return {"Respuesta":"Libro indixado con exito"} 

@router.post('/{book_id}')
def obtener_libro(book_id:UUID):
    for book in libros:
        #print(book,type(book))
        if book["id"] == book_id:
            return {"libro":book} 
    return{"respuesta":"Libro no encontrado"} 

@router.post('/obtener_libro')
def obtener_libro_2(book_id:Bookid): 
    for book in libros:
        if book["id"] == book_id.id:
            return{"libro":book}
    return{"respuesta":"Libro no encontrado"} 


@router.delete('/{book_id}')
def eliminar_libro(book_id:UUID):
    for index,book in enumerate(libros):
        if book["id"]==book_id:
            libros.pop(index)
            return{"Respuesta":"Libro eliminado correctamente"} 
    return{"respuesta":"Libro no encontrado"} 


@router.put('/{book_id}')
def actualizar_libro(book_id:UUID,updateuser:Book):
    for index,book in enumerate(libros):
        if book["id"]==book_id:
            libros[index]["id"] = updateuser.dict()["id"]    
            libros[index]["titulo"] = updateuser.dict()["titulo"]    
            libros[index]["autor"] = updateuser.dict()["autor"]    
            libros[index]["calificacion"] = updateuser.dict()["calificacion"]    
            return{"Respuesta":"Libro Actualizado correctamente"} 
    return{"respuesta":"Libro no encontrado"} 

