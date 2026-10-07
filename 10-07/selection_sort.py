import random

def trocar_posicao(l, i, j):
    aux = l[j]
    l[j] = l[i]
    l[i] = aux


def selection_sort(l):
    for i in range(len(l)):
        menor = l[i]
        menor_idx = i
        for j in range(i, len(l)):
            if l[j] < menor:
                menor = l[j]
                menor_idx = j

        trocar_posicao(l, i, menor_idx)

l = [random.randint(0, 20) for i in range(10)]
print(l)

selection_sort(l)
print(l)