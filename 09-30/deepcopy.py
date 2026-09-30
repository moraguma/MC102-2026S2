def deep_copy(matriz):
    """
        Copia uma matriz e as listas internas
    """
    resultado = []

    for linha in matriz:
        resultado.append(linha.copy())

    return resultado

a = [
    [1, 2, 3],
    [4, 5, 6]
]
b = deep_copy(a)

b[1][1] = 7
print(a)
print(b)