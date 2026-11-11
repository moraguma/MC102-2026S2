import csv
import matplotlib.pyplot as plt

with open("arquivos/coordenadas.csv", "r") as f:
    leitor = csv.DictReader(f)
    dados = list(leitor)

    xs = [float(dado["x"]) for dado in dados]
    ys = [float(dado["y"]) for dado in dados]

    plt.scatter(xs, ys)
    plt.savefig("11-11/scatter.png")