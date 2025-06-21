import requests

def get_exchange_rate(from_code: str, to_code: str) -> float | None:
    url = f"https://api.frankfurter.app/latest?amount=1&from={from_code.upper()}&to={to_code.upper()}"
    print(f" URL consultada: {url}")

    try:
        response = requests.get(url)
        print(f"Código HTTP: {response.status_code}")
        data = response.json()
        print(f" Resposta JSON: {data}")

       
        rate = data["rates"].get(to_code.upper())
        return rate
    except Exception as e:
        print(f" Erro ao buscar taxa: {e}")
        return None
