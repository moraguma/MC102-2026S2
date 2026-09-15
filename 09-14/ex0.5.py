palavra = input("Insira um palavra: ")
vogais = "aeiouAEIOUãÃ"
quantidade_de_vogais = 0
for char in palavra:
    if char in vogais:
        quantidade_de_vogais += 1

print(quantidade_de_vogais)