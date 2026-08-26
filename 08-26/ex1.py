n = int(input("Tamanho da lista: "))

lista_de_compras = []
i = 0
while i < n:
    lista_de_compras.append(input("Novo item: "))
    i += 1

item_a_checar = input()

encontrado = False
i = 0
while i < n:
    if lista_de_compras[i] == item_a_checar:
        encontrado = True
    i += 1

print(encontrado)