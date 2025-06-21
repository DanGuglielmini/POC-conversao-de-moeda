# app/main.py
from fastapi import FastAPI
from app.api.routes import router
from app.core.database import create_tables
from app.core.init_data import init_data

app = FastAPI()

@app.on_event("startup")
def startup():
    create_tables()
    init_data()

app.include_router(router)
@app.get("/")
def root():
    return {"message": "API está funcionando!"}
