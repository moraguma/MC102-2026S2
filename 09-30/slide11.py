def permutacao(matriz):
    # Verificar se só tem 0 e 1
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if not matriz[i][j] in [0, 1]:
                return False

    # Verificar linhas
    for i in range(len(matriz)):
        soma = 0
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
        if soma != 1:
            return False

    # Verificar colunas
    for j in range(len(matriz)):
        soma = 0
        for i in range(len(matriz[j])):
            soma += matriz[i][j]
        if soma != 1:
            return False

    return True


print(permutacao([
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0]
]))