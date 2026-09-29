def multiplica_matriz(a, b):
    """
        cij = sum(akj * bjk)
    """
    if len(a[0]) != len(b):
        return [[]]

    matriz = []
    for i in range(len(a)): # Linha atual
        linha = []
        for j in range(len(b[i])): # Coluna atual
            elemento = 0
            for k in range(len(a[i])): # Somatório
                elemento += a[i][k] * b[k][j]
            linha.append(elemento)
        matriz.append(linha)

    return matriz

[1 ,2 , 3, 4, 5, 6, 7, 8, 9]


def imprimir_matriz(m):
    """
        Imprime uma matriz de um jeito bonito
    """
    for linha in m:
        print(linha)


a = [
    [1, 2],
    [3, 4]
]

b = [
    [5],
    [6]
]

imprimir_matriz(multiplica_matriz(a, b))