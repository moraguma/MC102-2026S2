def sudoku(matriz):
    """
        Dado um jogo de sudoku, verifica se é solução válida
    """
    # Verificar se linhas são válidas
    for linha in matriz:
        elementos = linha.copy()
        elementos.sort()
        if elementos != list(range(1, 10)):
            return False

    # Verificar se colunas são válidas
    for j in range(len(matriz)):
        elementos = []
        for i in range(len(matriz[j])):
            elementos.append(matriz[i][j])
            
        elementos.sort()
        if elementos != list(range(1, 10)):
            return False

    # Verificando quadrados
    for i_comeco in range(3):
        for j_comeco in range(3):
            elementos = []
            for i in range(3 * i_comeco, 3 * i_comeco + 3):
                for j in range(3 * j_comeco, 3 * j_comeco + 3):
                    elementos.append(matriz[i][j])
            
            elementos.sort()
            if elementos != list(range(1, 10)):
                return False
    
    return True


matriz = [
    [4, 2, 6, 5, 7, 1, 3, 9, 8],
    [8, 5, 7, 2, 9, 3, 1, 4, 6],
    [1, 3, 9, 4, 6, 8, 2, 7, 5],
    [9, 7, 1, 3, 8, 5, 6, 2, 4],
    [5, 4, 3, 7, 2, 6, 8, 1, 9],
    [6, 8, 2, 1, 4, 9, 7, 5, 3],
    [7, 9, 4, 6, 3, 2, 5, 8, 1],
    [2, 6, 5, 8, 1, 4, 9, 3, 7],
    [3, 1, 8, 9, 5, 7, 4, 6, 2]
]
print(sudoku(matriz))