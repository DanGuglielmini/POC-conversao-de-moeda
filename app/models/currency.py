# app/models/currency.py
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)  # Ex: USD, EUR
    name = Column(String)  # Ex: Dólar Americano
    rate = Column(Float)  # Taxa em relação à moeda base (ex: BRL)
