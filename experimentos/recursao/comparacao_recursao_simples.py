import matplotlib.pyplot as plt
import time
from tqdm.auto import tqdm
import sys
sys.setrecursionlimit(10001)

def fatorial_rec(n):
    if n == 0:
        return 1
    return fatorial_rec(n - 1) * n

def fatorial_it(n): 
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def temporizar_algoritmo(f, n, ordenar=False, seeds=1):
	"""
		Mede o tempo de execução em segundos de um algoritmo recursivo f para n com uma quantidade de seeds
	"""
	total = 0
	for i in range(seeds):
		inicio = time.time()
		f(n)
		total += time.time() - inicio
	total /= seeds

	return total

algoritmos = [
	{"nome": "Iterativo", "func": fatorial_it},
	{"nome": "Recursivo", "func": fatorial_rec}
]

for algoritmo in algoritmos:
  algoritmo["resultados"] = []

for i in tqdm(range(1, 9000), desc="Rodando algoritmos", unit=" Valores de n"):
	for algoritmo in algoritmos:
		algoritmo["resultados"].append(temporizar_algoritmo(algoritmo["func"], i))

algoritmos[0]["mem"] = [1 for i in range(1, 9000)]
algoritmos[1]["mem"] = [i for i in range(1, 9000)]

fig, ax = plt.subplots(1, 2, figsize=(16,6))
for algoritmo in algoritmos:
  ax[0].plot(algoritmo["resultados"], label=algoritmo["nome"])
  ax[1].plot(algoritmo["mem"], label=algoritmo["nome"])

ax[0].set_ylabel("Tempo (s)")
ax[0].set_xlabel("Valor de n")
ax[0].legend()
ax[0].set_title("Tempo para rodar fatorial")

ax[1].set_ylabel("Chamadas de função na pilha")
ax[1].set_xlabel("Valor de n")
ax[1].legend()
ax[1].set_title("Custo de memória de fatorial")

fig.tight_layout()
fig.savefig("experimentos/recursao/comparacao_fatorial.png")