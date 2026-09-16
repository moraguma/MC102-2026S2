items = [
    {"Nome": "Banana", "Preço": 9.99, "Estoque": 1000},
    {"Nome": "Chocolate", "Preço": 10.0, "Estoque": 10},
    {"Nome": "Ovo", "Preço": 12.90, "Estoque": 600}
]

for item in items:
    print(f"{item['Nome']} - R${item['Preço']}")

produtos = {
    "Banana": {"Preço": 9.99, "Estoque": 1000},
    "Chocolate": {"Preço": 10.0, "Estoque": 10},
    "Ovo": {"Preço": 12.90, "Estoque": 600},
}

for chave in produtos:
    print(f"{chave} - R${produtos[chave]['Preço']}")

produtos = {
    "Banana": [9.99, 1000],
    "Chocolate": [10.0, 10],
    "Ovo": [12.9, 600],
}

for chave in produtos:
    print(f"{chave} - R${produtos[chave][0]}")