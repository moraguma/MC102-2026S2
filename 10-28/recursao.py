def hanoi(n, inicio, fim):
    if n == 1:
        print(f"Passe {inicio} para {fim}")
        return

    for i in range(3):
        if i != inicio and i != fim:
            aux = i
            break

    hanoi(n - 1, inicio, aux)
    print(f"Passe {inicio} para {fim}")
    hanoi(n - 1, aux, fim)


hanoi(4, 0, 2)
