lista_de_compras = ["Abacaxi", "Ovo", "Macarrão"]
preco_dos_itens = [9.99, 19.99, 3.99]
ids = [1, 2415135, 3214]

print(f"{lista_de_compras[0]} - R${preco_dos_itens[0]}")

meu_dicionario = {
    "Abacaxi": 9.99, 
    "Ovo": 19.99, 
    "Macarrão": 3.99
}

print(f"Abacaxi - R${meu_dicionario['Abacaxi']}")

meu_dicionario_tipado = {
    1.22: "Maçã",
    True: -1,
    (1, 2): "Macarrão"
}

print(meu_dicionario_tipado[(1, 2)])