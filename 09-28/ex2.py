def checar_matriz(matriz):
    if len(matriz) == 0:
        return False

    largura = len(matriz[0])
    for i in range(1, len(matriz)):
        if largura != len(matriz[i]):
            return False

    return True


matriz = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
]

print(checar_matriz(matriz))

nao_matriz = [
    [1, 2],
    [3, 4, 5],
    [6]
]

print(checar_matriz(nao_matriz))