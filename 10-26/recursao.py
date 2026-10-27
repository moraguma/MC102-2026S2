def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def fatorial_rec(n):
    if n == 0:
        return 1
    return fatorial_rec(n - 1) * n


print(fatorial_rec(6))