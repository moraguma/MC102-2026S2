def quadrado_magico(matriz):
    # Verificar números em (1, n x n)
    elementos = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            elementos.append(matriz[i][j])

    elementos.sort()
    if elementos != list(range(1, len(elementos) + 1)):
        return False

    # Verificar diagonal
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:
                soma += matriz[i][j]

    # Verificar diagonal secundária
    nova_soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i + j == len(matriz) - 1:
                nova_soma += matriz[i][j]
    if nova_soma != soma:
        return False

    # Verificar linhas
    for i in range(len(matriz)):
        nova_soma = 0
        for j in range(len(matriz[i])):
            nova_soma += matriz[i][j]
        if nova_soma != soma:
            return False

    # Verificar colunas
    for j in range(len(matriz)):
        nova_soma = 0
        for i in range(len(matriz[j])):
            nova_soma += matriz[i][j]
        if nova_soma != soma:
            return False

    return True


print(quadrado_magico(
    [
        [2, 7, 6],
        [9, 5, 1],
        [4, 3, 8]
    ]
))