def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_iterativo(n):
    menos_2 = 1
    menos_1 = 1
    for i in range(n - 1):
        resultado = menos_2 + menos_1
        menos_2 = menos_1
        menos_1 = resultado
    return resultado


print(fibonacci(50))