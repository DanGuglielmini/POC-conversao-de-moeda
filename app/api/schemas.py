from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ServicoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    valor: float
    moeda: str  # Ex: "USD"

class ServicoCreate(ServicoBase):
    pass

class ServicoOut(ServicoBase):
    id: int
    criado_em: datetime
    atualizado_em: Optional[datetime]

    class Config:
        orm_mode = True
