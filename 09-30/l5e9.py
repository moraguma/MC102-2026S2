def sem_volta_cidade(matriz, cidade):
    for cidade_dest in range(len(matriz)):
        if matriz[cidade][cidade_dest] == 1:
            return False

    for cidade_origem in range(len(matriz)):
        if matriz[cidade_origem][cidade] == 1:
            return True
    return False


def sem_volta(matriz):
    resultado = []
    for cidade in range(len(matriz)):
        resultado.append(sem_volta_cidade(matriz, cidade))
    return resultado


def so_volta_cidade(matriz, cidade):
    for cidade_origem in range(len(matriz)):
        if matriz[cidade_origem][cidade] == 1:
            return False

    for cidade_dest in range(len(matriz)):
        if matriz[cidade][cidade_dest] == 1:
            return True
    return False


def sem_nada_cidade(matriz, cidade):
    for cidade_origem in range(len(matriz)):
        if matriz[cidade_origem][cidade] == 1:
            return False

    for cidade_dest in range(len(matriz)):
        if matriz[cidade][cidade_dest] == 1:
            return False
    return True


def so_volta(matriz):
    resultado = []
    for cidade in range(len(matriz)):
        resultado.append(so_volta_cidade(matriz, cidade))
    return resultado





def sem_nada(matriz):
    resultado = []
    for cidade in range(len(matriz)):
        resultado.append(sem_nada_cidade(matriz, cidade))
    return resultado


print(sem_volta(
    [
        [0, 1, 1],
        [0, 0, 0],
        [1, 0, 0]
    ]
))