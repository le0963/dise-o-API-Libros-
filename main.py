from fastapi import FastAPI
import uvicorn
from app.routers import user
from app.routers import book

app = FastAPI()
app.include_router(user.router) 
app.include_router(book.router) 

if __name__=="__main__":
    uvicorn.run("main:app",port=8000,reload=True) 
