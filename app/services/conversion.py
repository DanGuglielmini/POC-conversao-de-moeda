# app/services/conversion.py
from sqlalchemy.orm import Session
from app.models.currency import Currency

def convert_currency(db: Session, from_code: str, to_code: str, amount: float):
    from_currency = db.query(Currency).filter(Currency.code == from_code.upper()).first()
    to_currency = db.query(Currency).filter(Currency.code == to_code.upper()).first()

    if not from_currency or not to_currency:
        return None
    
    usd_value = amount / from_currency.rate
    final_value = usd_value * to_currency.rate
    return round(final_value, 2)


    # valor convertido = valor_original * (taxa_destino / taxa_origem)
    converted_amount = amount * (to_currency.rate / from_currency.rate)
    return {
        "from": from_code,
        "to": to_code,
        "original_amount": amount,
        "converted_amount": round(converted_amount, 2)
    }
    
