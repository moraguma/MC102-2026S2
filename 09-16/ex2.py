# Entrada: <nome> <cpf> <idade>

n = int(input("Insira n: "))
informacoes = {}
for i in range(n):
    nome, cpf, idade = input("Insira nome, cpf e idade: ").split()
    if cpf in informacoes:
        continue

    informacoes[cpf] = {
        "Nome": nome,
        "Idade": idade
    }

print(informacoes)