x = int(input("Insira um número: "))

resto = x % 2
eh_par = resto == 0

if eh_par:
    # Par
    print("É par!")
else:
    # Ímpar
    print("É ímpar!")