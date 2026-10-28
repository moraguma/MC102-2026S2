def soma(n):
    if n == 1:
        return 1
    return soma(n - 1) + n


print(soma(2000))