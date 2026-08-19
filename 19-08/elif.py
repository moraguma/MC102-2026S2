idade = int(input("Qual a sua idade? "))

if idade <= 3:
    print("Bebê")
elif idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 25:
    print("Jovem adulto")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")