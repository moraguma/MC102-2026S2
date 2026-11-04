def balde_de_tinta(matriz, i, j):
    if i < 0 or i > len(matriz) - 1 or j < 0 or j > len(matriz[i]) - 1 or matriz[i][j] != 1:
        return 
    matriz[i][j] = 2

    balde_de_tinta(matriz, i + 1, j)
    balde_de_tinta(matriz, i - 1, j)
    balde_de_tinta(matriz, i, j + 1)
    balde_de_tinta(matriz, i, j - 1)


def imprime_matriz(matriz):
    for linha in matriz:
        print("".join([str(x) for x in linha]))


imagem = [
    [0, 1, 1],
    [1, 0, 1],
    [0, 1, 1]
]

balde_de_tinta(imagem, 0, 2)
imprime_matriz(imagem)