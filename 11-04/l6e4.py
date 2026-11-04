def soma_harmonica(n):
    if n == 1:
        return 1

    return soma_harmonica(n - 1) + 1 / n

print(soma_harmonica(4))
