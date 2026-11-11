import random


def merge(l1, l2):
    """
        Dados l1 e l2 ordenados, junta em uma com os dois, também ordenada
    """

    resultado = []
    i = 0
    j = 0

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            resultado.append(l1[i])
            i += 1
        else:
            resultado.append(l2[j])
            j += 1

    resultado += l1[i:]
    resultado += l2[j:]

    return resultado


def merge_sort(l, inicio, fim):
    if fim - inicio <= 1:
        return

    metade = (inicio + fim) // 2

    merge_sort(l, inicio, metade)
    merge_sort(l, metade, fim)

    l1 = l[inicio:metade]
    l2 = l[metade:fim]
    l[inicio:fim] = merge(l1, l2)


l = random.sample(range(10), 8)
merge_sort(l, 0, 8)
print(l)