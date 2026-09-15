palindromo = input("Insira uma palavra: ").lower().replace(" ", "")

tamanho_total = len(palindromo) // 2

eh_palindromo = True
for i in range(0, tamanho_total):
    if palindromo[i] != palindromo[len(palindromo) - i - 1]:
        eh_palindromo = False
        break

if eh_palindromo:
    print("Palíndromo")
else:
    print("Não é")