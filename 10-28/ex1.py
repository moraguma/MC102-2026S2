def binario(n):
    if n <= 1:
        return str(n)

    return binario(n // 2) + str(n % 2)


print(binario(10))