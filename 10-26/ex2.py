def soma_lista(l):
    resultado = 0
    for elemento in l:
        resultado += elemento
    return resultado


def soma_lista_rec(l, n):
    if n == 0:
        return 0

    return soma_lista_rec(l, n - 1) + l[n - 1]


l = [2, 4, 9, 14, 2, -2]
print(soma_lista(l))
print(soma_lista_rec(l, 6))