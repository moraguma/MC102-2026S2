import matplotlib.pyplot as plt
import time
from tqdm.auto import tqdm

def fibonacci_rec(n):
	if n == 1 or n == 2:
		return 1
	return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


def _fibonacci_mem(n, mem):
	if n == 1 or n == 2:
		return 1

	if not n - 1 in mem:
		mem[n - 1] = _fibonacci_mem(n - 1, mem)
	if not n - 2 in mem:
		mem[n - 2] = _fibonacci_mem(n - 2, mem)

	return mem[n - 1] + mem[n - 2]


def fibonacci_mem(n):
	return _fibonacci_mem(n, {})


def fibonacci_it(n):
	prev = 1
	prevprev = 1

	for i in range(n - 2):
		novo = prev + prevprev
		prevprev = prev
		prev = novo

	return prev


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
	{"nome": "Iterativo", "func": fibonacci_it},
	{"nome": "Recursivo", "func": fibonacci_rec},
	{"nome": "Recursivo com Memoização", "func": fibonacci_mem},
]

for algoritmo in algoritmos:
  algoritmo["resultados"] = []

for i in tqdm(range(1, 40), desc="Rodando algoritmos", unit=" Valores de n"):
	for algoritmo in algoritmos:
		algoritmo["resultados"].append(temporizar_algoritmo(algoritmo["func"], i))

fig, ax = plt.subplots(1, 1, figsize=(16,6))
for algoritmo in algoritmos:
  ax.plot(algoritmo["resultados"], label=algoritmo["nome"])

ax.set_ylabel("Tempo (s)")
ax.set_xlabel("Valor de n")
ax.legend()

ax.set_title("Comparação de implementações de Fibonacci")

fig.tight_layout()
fig.savefig("experimentos/recursao/comparacao_fibonacci_memoizacao.png")