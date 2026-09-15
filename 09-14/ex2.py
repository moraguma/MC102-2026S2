frase = input("Insira uma frase: ")
espacos = " \n\t"

total_de_palavras = 0
for i in range(1, len(frase)):
    if (not frase[i] in espacos) and (frase[i - 1] in espacos):
        total_de_palavras += 1

if not frase[0] in espacos:
    total_de_palavras += 1

print(total_de_palavras)