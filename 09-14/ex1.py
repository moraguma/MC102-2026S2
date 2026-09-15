entrada = [int(i) for i in input("Forneça uma sequência de números: ").split()]

media = 0
for i in entrada:
    media += i
media /= len(entrada)

print(media)