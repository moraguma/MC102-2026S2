import random


def busca_binaria(lista, x, inicio, fim):
    if inicio > fim:
        return -1
    if inicio == fim:
        if lista[inicio] == x:
            return inicio
        return -1

    meio = (inicio + fim) // 2
    if lista[meio] == x:
        return meio
    if lista[meio] < x:
        return busca_binaria(lista, x, meio + 1, fim)
    if lista[meio] > x:
        return busca_binaria(lista, x, inicio, meio - 1)



lista = random.sample(range(30), 20)
lista.sort()
print(lista)
print(busca_binaria(lista, 20, 0, len(lista) - 1))