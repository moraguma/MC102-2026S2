def eh_divisor(a, b):
    return a % b == 0


def encontrar_divisores_proprios(a):
    divisores = []
    for b in range(1, a):
        if eh_divisor(a, b):
            divisores.append(b)
    return divisores


def soma_lista(lista):
    resultado = 0
    for item in lista:
        resultado += item
    return resultado


def sao_amigos(a, b):
    a_ok_b = soma_lista(encontrar_divisores_proprios(a)) == b
    b_ok_a = soma_lista(encontrar_divisores_proprios(b)) == a
    return a_ok_b and b_ok_a


for i in range(1, 2000):
    for j in range(i, 2000):
        if sao_amigos(i, j):
            print(i, j)