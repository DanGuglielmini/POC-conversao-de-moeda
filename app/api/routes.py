# app/api/routes.py
from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.conversion import convert_currency
from app.utils.i18n import translate
from app.services.external_api import get_exchange_rate

router = APIRouter()

@router.post("/convert")
def convert(
    request: Request,
    from_code: str,
    to_code: str,
    amount: float,
    db: Session = Depends(get_db)
):
    rate = get_exchange_rate(from_code, to_code)
    
    if rate is None:
        return {"erro": translate(request, "currency_not_found"),
                "detalhe": f"De {from_code} para {to_code}"
         }
    
    converted = round(amount * rate, 2)
    return {
        "de": from_code.upper(),
        "para": to_code.upper(),
        "valor_inicial": amount,
        "valor_convertido": converted,
        "cotacao_usada": rate
    }
