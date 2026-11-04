def cidades_alcancaveis(adjacencias, i, mem):
    """
        mem -> Lista de cidades alcançadas
    """
    mem.append(i)

    for j in range(len(adjacencias[i])):
        if adjacencias[i][j] == 1 and j not in mem:
            cidades_alcancaveis(adjacencias, j, mem)


cidades = []
adjacencias = [
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
cidades_alcancaveis(adjacencias, 0, cidades)
print(cidades)