def ler_matriz():
    matriz = []
    while True:
        linha = input()
        if linha == "":
            break

        matriz.append(list(linha))
    return matriz


def imprime_matriz(matriz):
    for linha in matriz:
        print("".join(linha))