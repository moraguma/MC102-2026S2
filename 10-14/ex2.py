
def busca_binaria_mod(l, x):
    """
        Procura x em l e, se encontrar, retorna sua posição. Só
        funciona se l estiver ordenada
    """
    pos_ini = 0
    pos_fim = len(l) - 1

    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2
        if l[pos_meio] == x:
            return pos_meio
        elif l[pos_meio] > x:
            pos_fim = pos_meio - 1
        else:
            pos_ini = pos_meio + 1
    return pos_ini


l = list(range(2, 37, 2))
x = 13

print(busca_binaria_mod(l, x))
