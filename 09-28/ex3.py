def calcula_transposta(matriz):
    transposta = []
    for i in range(len(matriz)):
        linha = []
        for j in range(len(matriz[i])):
            linha.append(matriz[j][i])
        transposta.append(linha)
    return transposta

def imprimir_matriz(m):
    """
        Imprime uma matriz de um jeito bonito
    """
    for linha in m:
        print(linha)

m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

imprimir_matriz(m)
print()
imprimir_matriz(calcula_transposta(m))