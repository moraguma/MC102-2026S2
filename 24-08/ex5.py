n = int(input("n = "))

if n >= 1:
    maior = float(input())
    i = 1
    while i < n:
        novo_numero = float(input())

        if novo_numero > maior:
            maior = novo_numero

        i += 1 

    print(maior)