"""Baixa o arquivo de dados do estudo do METR para a pasta dados/brutos/."""
from datetime import date
from pathlib import Path
from urllib.request import urlretrieve

URL = "https://raw.githubusercontent.com/METR/Measuring-Early-2025-AI-on-Exp-OSS-Devs/main/data_complete.csv"
DESTINO = Path(__file__).parent / "dados" / "brutos" / "data_complete.csv"

DESTINO.parent.mkdir(parents=True, exist_ok=True)
urlretrieve(URL, DESTINO)

print(f"Arquivo salvo em {DESTINO}")
print(f"Data de acesso: {date.today():%d/%m/%Y} (anotem no README)")
