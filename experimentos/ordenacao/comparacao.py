import matplotlib.pyplot as plt
import time
import random
from tqdm.auto import tqdm

from algoritmos_ordenacao import bubble_sort, selection_sort, insertion_sort


def func_linear(l):
	"""
		Função linear pouco eficiente, para comparar com algoritmos de verdade
	"""
	for i in range(50000):
		l[0] = i
  
	for i in range(len(l)):
		for j in range(500):
			l[i] = j


def temporizar_algoritmo(f, n, ordenar=False, seeds=1):
	"""
		Mede o tempo de execução em segundos de um algoritmo de ordenação f em
		<seeds> listas de tamanho n
	"""
	total = 0
	for i in range(seeds):
		if ordenar:
			l = [i for i in range(n)]
		else:
			l = [random.randint(1, n) for i in range(n)]

		inicio = time.time()
		f(l)
		total += time.time() - inicio
	total /= seeds

	return total


algoritmos = [
	{"nome": "Bubble Sort", "func": bubble_sort},
	{"nome": "Selection Sort", "func": selection_sort},
	{"nome": "Insertion Sort", "func": insertion_sort},
	{"nome": "Função linear", "func": func_linear}
]

for algoritmo in algoritmos:
  algoritmo["resultados"] = []
  algoritmo["resultados_preordenado"] = []

for i in tqdm(range(1, 1501), desc="Rodando algoritmos", unit=" Listas"):
	for algoritmo in algoritmos:
		algoritmo["resultados"].append(temporizar_algoritmo(algoritmo["func"], i))
		algoritmo["resultados_preordenado"].append(temporizar_algoritmo(algoritmo["func"], i, True))

fig, axes = plt.subplots(1, 2, figsize=(16,6))
for algoritmo in algoritmos:
  axes[0].plot(algoritmo["resultados"], label=algoritmo["nome"])
  axes[1].plot(algoritmo["resultados_preordenado"], label=algoritmo["nome"])

for ax in axes:
	ax.set_ylabel("Tempo (s)")
	ax.set_xlabel("Tamanho da lista")
	ax.legend()

axes[0].set_title("Tempo de ordenação (aleatório)")
axes[1].set_title("Tempo de ordenação (pré ordenado)") 

fig.tight_layout()
fig.savefig("experimentos/ordenacao/comparacao_ordenacao.png")