meu_dicionario = {
    "Nome": "Macarrão",
    "Estoque": 247,
    "Preço": 3.99,
    "Cor": "Amarelo"
}

for key in meu_dicionario.keys():
    print(key)

for value in meu_dicionario.values():
    print(value)

for key, value in meu_dicionario.items():
    print(key, value)