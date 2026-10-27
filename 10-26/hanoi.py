def hanoi(n, inicial, final):
    """
        n -> Total de discos
        inicial -> Pino inicial pode ser 0, 1 ou 2
        final -> Pino final pode ser 0, 1 ou 2
    """
    if n == 1:
        print(f"Passe de {inicial} para {final}")
        return

    for i in range(3):
        if i != inicial and i != final:
            aux = i
            break

    hanoi(n - 1, inicial, aux)
    print(f"Passe de {inicial} para {final}")
    hanoi(n - 1, aux, final)


hanoi(3, 0, 2)