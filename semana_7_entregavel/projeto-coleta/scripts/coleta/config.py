from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    base_url: str = "http://127.0.0.1:8080"
    banco: str = "dados/vagas.db"
    pasta_logs: str = "logs"
    espera: float | None = None
    timeout: tuple[float, float] = (3.05, 10.0)    # (conexão, leitura)
    max_tentativas: int = 4
    espera_base: float = 0.5
    espera_maxima: float = 30.0
    max_paginas: int = 20
    user_agent: str = (
        "ColetatronMurais/1.0 (projeto de estudo; contato: pedrohg0505@gmail.com)"
    )