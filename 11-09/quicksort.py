import random


def trocar_elementos(l, i, j):
    aux = l[i]
    l[i] = l[j]
    l[j] = aux


def partition(lista, inicio, fim):
    j = inicio

    for i in range(inicio + 1, fim):
        if lista[i] <= lista[inicio]:
            j += 1
            trocar_elementos(lista, i, j)
    trocar_elementos(lista, inicio, j)
    return j


def quick_sort(lista, inicio, fim):
    if fim - inicio <= 1:
        return

    pivo = partition(lista, inicio, fim)
    quick_sort(lista, inicio, pivo)
    quick_sort(lista, pivo + 1, fim)


l = random.sample(range(10), 8)
print(l)
quick_sort(l, 0, 8)
print(l)