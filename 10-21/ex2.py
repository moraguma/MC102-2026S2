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


def encontrar(matriz, x):
    """
        Encontra a posição de x na matriz
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == x:
                return (i, j)


tabuleiro = ler_matriz()
pos_atual = encontrar(tabuleiro, "K")

pos_futura = input("Passe a posição futura: ").split(",")
pos_futura[0] = int(pos_futura[0])
pos_futura[1] = int(pos_futura[1])

if pos_futura[0] in range(len(tabuleiro)) and pos_futura[1] in range(len(tabuleiro[0])):
    diferenca_absoluta = (abs(pos_futura[0] - pos_atual[0]), abs(pos_futura[1] - pos_atual[1]))
    if diferenca_absoluta == (2, 1) or diferenca_absoluta == (1, 2):
        # Pos inicial do K
        tabuleiro[pos_atual[0]][pos_atual[1]] = "."
        # Pos final do K
        tabuleiro[pos_futura[0]][pos_futura[1]] = "K"

imprime_matriz(tabuleiro)
