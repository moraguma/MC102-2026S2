import csv
import matplotlib.pyplot as plt

with open("arquivos/elevacao.csv", "r") as f:
    leitor = csv.DictReader(f)
    dados = list(leitor)

    xs = [float(dado["x"]) for dado in dados]
    ys = [float(dado["y"]) for dado in dados]
    zs = [float(dado["altura"]) for dado in dados]

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_trisurf(xs, ys, zs)
    plt.savefig("11-11/elevacao.png")