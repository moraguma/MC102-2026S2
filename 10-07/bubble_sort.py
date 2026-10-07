import random

def trocar_posicao(l, i, j):
    aux = l[j]
    l[j] = l[i]
    l[i] = aux


def bubble_sort(l):
    for i in range(len(l)):
        ordenado = True

        for j in range(1, len(l) - i):
            if l[j] < l[j - 1]:
                ordenado = False
                trocar_posicao(l, j, j - 1)

        if ordenado:
            break


l = [random.random() for i in range(10)]
print(l)

bubble_sort(l)
print(l)

bubble_sort([1, 2, 3, 4, 5, 6])