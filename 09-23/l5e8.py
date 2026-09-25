import random


def histograma(lista):
    """
        [1, 2, 4, 4, 2, 2]

        vira

        {
            1: 1,
            2: 3,
            4: 2
        }
    """
    hist = {}
    for i in lista:
        hist[i] = lista.count(i)
    return hist


def frequencias(lista):
    menor_frequencia = len(lista) + 1
    menos_frequente = -1
    maior_frequencia = 0
    mais_frequente = -1

    hist = histograma(lista)
    for numero in hist:
        if hist[numero] < menor_frequencia:
            menor_frequencia = hist[numero]
            menos_frequente = numero
        if hist[numero] > maior_frequencia:
            maior_frequencia = hist[numero]
            mais_frequente = numero

    return (menos_frequente, mais_frequente)


lista = [random.randint(1, 10) for i in range(20)]
print(lista)
print(frequencias(lista))