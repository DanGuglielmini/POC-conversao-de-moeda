from fastapi import FastAPI
from app.api.servicos import router as servicos_router
from app.core.database import create_tables
from app.core.init_data import init_data

app = FastAPI()

@app.on_event("startup")
def startup():
    create_tables()  
    init_data()      

app.include_router(servicos_router)

@app.get("/")
def root():
    return {"message": "API está funcionando!"}
