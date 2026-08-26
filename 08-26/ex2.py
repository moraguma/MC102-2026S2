n = int(input("Tamanho da lista: "))

lista_de_compras = []
i = 0
while i < n:
    lista_de_compras.append(input("Novo item: "))
    i += 1

while True:
    print(lista_de_compras)
    item_a_remover = input("O que foi comprado? ")

    i = 0
    while i < len(lista_de_compras):
        if lista_de_compras[i] == item_a_remover:
            lista_de_compras[i] = "COMPRADO" 
            break
        i += 1

    terminada = True
    i = 0
    while i < len(lista_de_compras):
        if lista_de_compras[i] != "COMPRADO":
            terminada = False
        i += 1

    if terminada:
        break