import requests

BASE = "http://127.0.0.1:8080"

padrao = requests.get(f"{BASE}/eco", timeout=10).json()
print("User-Agent padrão:", padrao["user-agent"])

USER_AGENT = "ColetatronMurais/1.0 (projeto de estudo; contato: pedrohg0505@gmail.com)"
sessao = requests.Session()
sessao.headers["User-Agent"] = USER_AGENT

def baixar(sessao, url):
    resposta = sessao.get(url, timeout=(3.05, 10))
    resposta.raise_for_status()
    return resposta
