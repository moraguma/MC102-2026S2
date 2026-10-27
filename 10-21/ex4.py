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
                return [i, j]


labirinto = ler_matriz()
pos = encontrar(labirinto, "E")
estados = []


vel = [0, 1]
t = 0
while True:
    preso = False
    for estado in estados:
        if pos == estado["pos"] and vel == estado["vel"]:
            print("GAME OVER!")
            preso = True
            break 
    if preso:
        break

    estados.append({
        "pos": pos.copy(),
        "vel": vel.copy()
    })
    
    while True:
        # Verificar se vai bater
        nova_posicao = (pos[0] + vel[0], pos[1] + vel[1])

        bateu = False
        if not nova_posicao[0] in range(len(labirinto)) or not nova_posicao[1] in range(len(labirinto[0])):
            bateu = True

        if not bateu:
            if labirinto[nova_posicao[0]][nova_posicao[1]] == "#":
                bateu = True

        if not bateu:
            break

        if bateu: # Rotacionar
            if vel[0] == 0 and vel[1] == 1:
                vel[0] = 1
                vel[1] = 0
            elif vel[0] == 1 and vel[1] == 0:
                vel[0] = 0
                vel[1] = -1
            elif vel[0] == 0 and vel[1] == -1:
                vel[0] = -1
                vel[1] = 0
            else:
                vel[0] = 0
                vel[1] = 1
                

    # Mover de acordo com velocidade
    pos[0] += vel[0]
    pos[1] += vel[1]
    t += 1

    if labirinto[pos[0]][pos[1]] == "S":
        print(t)
        break
