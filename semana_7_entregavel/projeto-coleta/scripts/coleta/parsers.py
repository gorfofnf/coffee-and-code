from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

BASE = "http://127.0.0.1:8080"

def texto(tag):
    return tag.get_text(strip=True) if tag is not None else None

def ler_html(resposta) -> BeautifulSoup:
    return BeautifulSoup(resposta.content, "lxml")

def ler_cartao(cartao):
    return {
        "id": cartao["data-id"],
        "titulo": texto(cartao.select_one("h2.titulo a")),
        "empresa": texto(cartao.select_one(".empresa")),
        "local": texto(cartao.select_one(".local")),
        "salario": texto(cartao.select_one(".salario")),
        "publicada": cartao.select_one("time")["datetime"],
        "tags": [li.get_text(strip=True) for li in cartao.select("ul.tags li")],
        "link": cartao.select_one("h2.titulo a")["href"],
    }

def ler_cartao_vaga(cartao, url_pagina: str) -> dict:
    link = cartao.select_one("h2.titulo a")
    hora = cartao.select_one("time")
    return {
        "id_externo": cartao["data-id"],
        "titulo": texto(link),
        "empresa": texto(cartao.select_one(".empresa")),
        "local": texto(cartao.select_one(".local")),
        "modalidade": texto(cartao.select_one(".modalidade")),
        "nivel": texto(cartao.select_one(".nivel")),
        "salario": texto(cartao.select_one(".salario")),
        "publicada": hora["datetime"] if hora is not None else None,
        "tags": [li.get_text(strip=True) for li in cartao.select("ul.tags li")],
        "url": urljoin(url_pagina, link["href"]) if link is not None else None,
    }

def proxima_pagina(sopa, url_pagina: str) -> str | None:
    link = sopa.select_one("a[rel=next]")
    return urljoin(url_pagina, link["href"]) if link is not None else None

def ler_descricao(sopa) -> str | None:
    return texto(sopa.select_one(".descricao"))

def ler_vagas_da_pagina(sopa, url_pagina: str) -> list[dict]:
    return [ler_cartao_vaga(c, url_pagina) for c in sopa.select("article.vaga")]

def ler_eventos(sopa, url_pagina: str) -> list[dict]:
    eventos = []
    for item in sopa.select("li.evento"):
        link = item.select_one("h3 a")
        eventos.append({
            "id_externo": item["data-id"],
            "titulo": texto(link),
            "quando": texto(item.select_one(".quando")),
            "onde": texto(item.select_one(".onde")),
            "preco": texto(item.select_one(".preco")),
            "organizacao": texto(item.select_one(".organizacao")),
            "url": (urljoin(url_pagina, link["href"])
                    if link is not None else None),
        })
    return eventos
