import requests


url = "http://127.0.0.1:8000/v1/forecast"
params = {
    "latitude": -26.4851,
    "longitude": -49.0713,
    "current": "temperature_2m"
}

resposta = requests.get(url, params=params)

if resposta.status_code == 200:
    dados = resposta.json()
else:
    print("Erro:", resposta.status_code, resposta.text)