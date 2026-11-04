def hanoi_modificado(n, inicio, final):
    for i in range(3):
        if i != inicio and i != final:
            aux = i
            break

    if n == 1:
        if abs(final - inicio) == 1:
            print(f"Passe de {inicio} para {final}")
        else:
            print(f"Passe de {inicio} para {aux}")
            print(f"Passe de {aux} para {final}")

        return

    hanoi_modificado(n - 1, inicio, final)
    print(f"Passe de {inicio} para {aux}")
    hanoi_modificado(n - 1, final, inicio)
    print(f"Passe de {aux} para {final}")
    hanoi_modificado(n - 1, inicio, final)


hanoi_modificado(3, 0, 2)