from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.servico import Servico
from app.services.conversion import convert_currency
from app.api.schemas import ServicoCreate, ServicoOut
from typing import List, Optional

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/servicos", response_model=ServicoOut)
def criar_servico(servico: ServicoCreate, db: Session = Depends(get_db)):
    novo = Servico(**servico.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/servicos", response_model=List[ServicoOut])
def listar_servicos(db: Session = Depends(get_db)):
    return db.query(Servico).all()

@router.get("/servicos/{id}", response_model=ServicoOut)
def obter_servico(id: int, db: Session = Depends(get_db)):
    servico = db.query(Servico).get(id)
    if not servico:
        raise HTTPException(status_code=404, detail="Serviço não encontrado.")
    return servico

@router.get("/servicos/{id}/converter")
def converter_valor_servico(
    id: int,
    para_moeda: str = Query(..., alias="para"),
    db: Session = Depends(get_db)
):
    servico = db.query(Servico).get(id)
    if not servico:
        raise HTTPException(status_code=404, detail="Serviço não encontrado.")

    convertido = convert_currency(
        db,
        from_code=servico.moeda,
        to_code=para_moeda.upper(),
        amount=float(servico.valor)
    )

    if convertido is None:
        raise HTTPException(status_code=400, detail="Conversão não disponível.")

    return {
        "nome": servico.nome,
        "valor_original": float(servico.valor),
        "moeda_original": servico.moeda,
        "valor_convertido": convertido,
        "moeda_destino": para_moeda.upper()
    }
@router.get("/teste")
def teste():
    return {"ok": True}
def rota_teste():
    return {"mensagem": "Funcionando"}