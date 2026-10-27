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


labirinto = ler_matriz()

quantidade_bolas = int(input("Quantidade bolas: "))
bolas = []
for i in range(quantidade_bolas):
    info = input("Nova bola: ").split()

    posicao_separada = info[0].split(",")
    posicao = [int(posicao_separada[0]), int(posicao_separada[1])]

    velocidade_separada = info[1].split(",")
    velocidade = (int(velocidade_separada[0]), int(velocidade_separada[1]))

    bolas.append({
        "pos": posicao,
        "vel": velocidade 
    })

t = 0
while True:
    for bola in bolas:
        bola["pos"][0] += bola["vel"][0]
        bola["pos"][1] += bola["vel"][1]
    t += 1

    colidiu = False
    for bola in bolas:
        # Saiu do labirinto
        if not bola["pos"][0] in range(len(labirinto)) or not bola["pos"][1] in range(len(labirinto[0])):
            colidiu = True
            break

        # Bateu em parede
        if labirinto[bola["pos"][0]][bola["pos"][1]] == "#":
            colidiu = True
            break

        # Bateu em uma bola
        for outra_bola in bolas:
            if outra_bola == bola:
                continue

            if bola["pos"][0] == outra_bola["pos"][0] and bola["pos"][1] == outra_bola["pos"][1]:
                colidiu = True
                break

    if colidiu:
        print(t)
        break