import matplotlib.pyplot as plt
import time
import random
from tqdm.auto import tqdm

import sys
sys.path.append("experimentos/ordenacao")
from algoritmos_busca import busca_sequencial, busca_binaria
from algoritmos_ordenacao import bubble_sort


def temporizar_algoritmo(f, l, x):
	"""
		Mede o tempo de execução em segundos de um algoritmo de busca f para encontrar x
		na lista l
	"""
	inicio = time.time()
	f(l, x)
	return time.time() - inicio


algoritmos = [
	{"nome": "Busca Sequencial", "func": busca_sequencial, "ordenar": False},
	{"nome": "Busca Binária", "func": busca_binaria, "ordenar": True}
]

for algoritmo in algoritmos:
  algoritmo["resultado_aleatorio"] = []
  algoritmo["resultado_com_ordenacao"] = []
  algoritmo["resultado_busca_inicio"] = []

range_sem_busca = range(1, 100000, 500)
for i in tqdm(range_sem_busca, desc="Rodando algoritmos", unit=" Buscas"):
	for algoritmo in algoritmos:
		algoritmo["resultado_aleatorio"].append(0)
		algoritmo["resultado_busca_inicio"].append(0)
		sementes = 10
		for j in range(sementes): # Repetir o experimento e pegar a média
			l = random.sample(range(1, i + 1), i)

			algoritmo["resultado_aleatorio"][len(algoritmo["resultado_aleatorio"]) - 1] += temporizar_algoritmo(algoritmo["func"], l, l[random.randint(0, i - 1)])
			algoritmo["resultado_busca_inicio"][len(algoritmo["resultado_aleatorio"]) - 1] += temporizar_algoritmo(algoritmo["func"], l, l[0])
		algoritmo["resultado_aleatorio"][len(algoritmo["resultado_aleatorio"]) - 1] /= sementes
		algoritmo["resultado_busca_inicio"][len(algoritmo["resultado_aleatorio"]) - 1] /= sementes
		

for i in tqdm(range(1, 1501), desc="Rodando algoritmos (com nosso Bubble Sort)", unit=" Buscas"):
	for algoritmo in algoritmos:
		l = random.sample(range(1, i + 1), i)

		tempo_ordenacao = 0
		if algoritmo["ordenar"]:
			inicio = time.time()
			bubble_sort(l)
			tempo_ordenacao += time.time() - inicio

		resultado = temporizar_algoritmo(algoritmo["func"], l, l[random.randint(0, i - 1)])
		algoritmo["resultado_com_ordenacao"].append(resultado + tempo_ordenacao)

fig, axes = plt.subplots(1, 3, figsize=(16,6))
for algoritmo in algoritmos:
  axes[0].plot(range_sem_busca, algoritmo["resultado_aleatorio"], label=algoritmo["nome"])
  axes[1].plot(algoritmo["resultado_com_ordenacao"], label=algoritmo["nome"])
  axes[2].plot(range_sem_busca, algoritmo["resultado_busca_inicio"], label=algoritmo["nome"])

for ax in axes:
	ax.set_ylabel("Tempo (s)")
	ax.set_xlabel("Tamanho da lista")
	ax.legend()

axes[0].set_title("Tempo de busca (elemento aleatório)")
axes[1].set_title("Tempo de busca contando ordenação (elemento aleatório)")
axes[2].set_title("Tempo de busca (sempre primeiro elemento)") 

fig.tight_layout()
fig.savefig("experimentos/busca/comparacao_busca.png")