x = int(input("x = "))
y = int(input("y = "))

resultado = 1 # Variável acumuladora -> Guardar um
i = 0         # Variável de iteração -> Conta
while i < y:
    resultado *= x
    i += 1

print(resultado)