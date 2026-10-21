def busca_linear(l, x):
    """
        Procura x em l e, se encontrar, retorna sua posição
    """
    for i in range(len(l)):
        if l[i] == x:
            return i

    return -1


l = [2, 13, 6, 313, 7, 1]
x = 99
print(busca_linear(l, x))