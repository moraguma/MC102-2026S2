sabores = ["Marguerita", "Calabresa", "4 Queijos", "Escarola", "M&M", "Nutella"]

while True:
    print("Selecione a opção desejada:")
    for i in range(len(sabores)):
        print(i + 1, "-", sabores[i])
    print(len(sabores) + 1, "- Sair")

    entrada = int(input())
    if entrada >= len(sabores) + 1:
        break
    else:
        print(sabores[entrada - 1])