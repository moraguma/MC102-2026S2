import json


with open("arquivos/exemplo.json") as f:
    dados = json.load(f)
    print(dados)