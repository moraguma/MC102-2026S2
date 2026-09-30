def verificar_triangular_inferior(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i < j and matriz[i][j] != 0:
                return False
    return True


matriz = [
    [1, 0, -1],
    [0, -3, 0],
    [1, 0, 2]
]
print(verificar_triangular_inferior(matriz))