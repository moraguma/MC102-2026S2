def encontrar_divisores_proprios(a):
    divisores = []
    for b in range(1, a):
        if a % b == 0:
            divisores.append(b)
    return divisores


def eh_primo(a):
    return len(encontrar_divisores_proprios(a)) == 1


def primeiro_primo_dif(a, dif):
    while True:
        a += dif
        if eh_primo(a):
            return a


def primeiro_primo_antes(a):
    if a <= 2:
        return -1
    return primeiro_primo_dif(a, -1)


def primeiro_primo_depois(a):
    return primeiro_primo_dif(a, 1)


def sanduiche_primo(a):
    return (primeiro_primo_antes(a), primeiro_primo_depois(a))

print(sanduiche_primo(int(input("n = "))))