import requests
from bs4 import BeautifulSoup
from coleta.parsers import ler_cartao, texto

BASE = "http://127.0.0.1:8080"

resposta = requests.get(f"{BASE}/vagas/", timeout=10)
resposta.raise_for_status()
sopa = BeautifulSoup(resposta.content, "lxml")

vagas = [ler_cartao(c) for c in sopa.select("article.vaga")]
print("vagas extraídas:", len(vagas))

print(vagas[0])