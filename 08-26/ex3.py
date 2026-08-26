lista = [2, 5, 23, 5, 1, -2]
lista.sort()

print(lista)
if len(lista) % 2 == 1:
    mediana = lista[(len(lista) - 1) // 2]
else:
    n1 = lista[len(lista) // 2 - 1]
    n2 = lista[len(lista) // 2]
    mediana = (n1 + n2) / 2
print(mediana)