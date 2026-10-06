def montar_labirinto():
    labirinto = []
    while True:
        entrada = input()
        if entrada == "":
            return labirinto

        linha = []
        for char in entrada:
            linha.append(char)
        labirinto.append(linha)


def imprimir_labirinto(labirinto):
    for linha in labirinto:
        print("".join(linha))
    print()


def encontrar_jogador(labirinto):
    """
        Retorna posição do jogador
    """
    for i in range(len(labirinto)):
        for j in range(len(labirinto[i])):
            if labirinto[i][j] == "J":
                return (i, j)



def mover(labirinto, i_delta, j_delta):
    """
        Dado x e y, move o jogador x na horizontal e y na vertical.
        Modifica o labirinto e retorna se o jogo acabou
    """
    pos = encontrar_jogador(labirinto)
    nova_pos = (pos[0] + i_delta, pos[1] + j_delta)

    if nova_pos[0] < 0 or nova_pos[0] >= len(labirinto) or \
            nova_pos[1] < 0 or nova_pos[1] >= len(labirinto[nova_pos[0]]):
        return False

    if labirinto[nova_pos[0]][nova_pos[1]] == "#":
        return False

    if labirinto[nova_pos[0]][nova_pos[1]] == "S":
        venceu = True
    else:
        venceu = False

    labirinto[pos[0]][pos[1]] = "-"
    labirinto[nova_pos[0]][nova_pos[1]] = "J"
    return venceu

    


def jogar(labirinto):
    while True:
        entrada = input()
        if entrada == "w":
            if mover(labirinto, -1, 0):
                break
        elif entrada == "a":
            if mover(labirinto, 0, -1):
                break
        elif entrada == "s":
            if mover(labirinto, 1, 0):
                break
        elif entrada == "d":
            if mover(labirinto, 0, 1):
                break

        imprimir_labirinto(labirinto)
    imprimir_labirinto(labirinto)



labirinto = montar_labirinto()
jogar(labirinto)