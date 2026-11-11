import csv


with open("11-11/exemplo.csv") as f:
    leitor = csv.reader(f)
    dados = list(leitor)

    for linha in dados:
        print(linha)