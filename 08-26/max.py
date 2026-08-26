minha_lista = [2, 6, 1, 20, -3, 7]

max = minha_lista[0]
i = 1
while i < len(minha_lista):
    if minha_lista[i] > max:
        max = minha_lista[i]

    i += 1

print(max)