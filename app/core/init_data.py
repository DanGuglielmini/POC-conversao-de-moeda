from app.core.database import SessionLocal
from app.models.currency import Currency

def init_data():
    db = SessionLocal()
    moedas = [
        {"code": "USD", "name": "Dólar Americano", "rate": 1.0},
        {"code": "BRL", "name": "Real Brasileiro", "rate": 5.5},
        {"code": "EUR", "name": "Euro", "rate": 0.85},
    ]
    for moeda in moedas:
        if not db.query(Currency).filter_by(code=moeda["code"]).first():
            db.add(Currency(**moeda))
    db.commit()
    db.close()
