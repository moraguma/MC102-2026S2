def soma_matriz(a, b):
    # cij = aij + bij
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        return [[]]

    resultado = []
    for i in range(len(a)):
        linha = []
        for j in range(len(a[i])):
            linha.append(a[i][j] + b[i][j])
        resultado.append(linha)   

    return resultado         

def imprimir_matriz(m):
    """
        Imprime uma matriz de um jeito bonito
    """
    for linha in m:
        print(linha)

a = [
    [1, 2],
    [3, 4],
    [5, 6]
]

b = [
    [5, 6],
    [1, 3],
    [4, 2]
]

imprimir_matriz(soma_matriz(a, b))