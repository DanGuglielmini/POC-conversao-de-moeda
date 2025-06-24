from sqlalchemy import Column, Integer, String, Numeric, DateTime, func
from app.core.database import Base

class Servico(Base):
    __tablename__ = "servicos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String)
    valor = Column(Numeric(10, 2), nullable=False)
    moeda = Column(String(3), nullable=False)  # Ex: 'USD', 'BRL'
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
    atualizado_em = Column(DateTime(timezone=True), onupdate=func.now())
