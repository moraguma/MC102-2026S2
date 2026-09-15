# entrada = input("Digite dois números: ").split()

# entrada_transformada = []
# for i in entrada:
#     entrada_transformada.append(int(i))
# x = entrada_transformada[0]
# y = entrada_transformada[1]

x, y = [int(i) for i in input("Digite dois números: ").split()]

print(x + y)
