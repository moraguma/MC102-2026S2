import csv
import json
import matplotlib.pyplot as plt


with open("arquivos/bolsa.json") as f:
    configs = json.load(f)

for arquivo in configs["arquivos"]:
    with open(f"arquivos/{arquivo['arquivo']}") as f:
        dados = list(csv.DictReader(f))

        xs = [float(dado["x"]) for dado in dados]
        ys = [float(dado["y"]) for dado in dados]

        plt.plot(xs, ys, label=arquivo["nome"])

plt.legend()
plt.savefig("11-11/bolsa.png")