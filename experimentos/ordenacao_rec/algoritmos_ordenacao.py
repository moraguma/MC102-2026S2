def trocar_elementos(l, i, j):
	"""
		Troca os elementos nas posições i e j da lista l de posição
	"""
	aux = l[i]
	l[i] = l[j]
	l[j] = aux


def bubble_sort(l):
	"""
		Ordena uma lista de forma crescente
	"""
	for i in range(len(l)):
		for j in range(1, len(l) - i):
			if l[j - 1] > l[j]:
				trocar_elementos(l, j - 1, j)


def indice_menor(l, p):
	"""
		Retorna o índice do menor elemento da lista, contando a partir da
		posição p
	"""
	idx_menor = p
	menor = l[p]

	for i in range(p + 1, len(l)):
		if l[i] < menor:
			idx_menor = i
			menor = l[i]
		
	return idx_menor


def selection_sort(l):
	"""
		Ordena uma lista de forma crescente
	"""
	for i in range(len(l) - 1):
		idx_menor = indice_menor(l, i)
		trocar_elementos(l, i, idx_menor)


def inserir(l, p):
	"""
		Supondo que a lista l está ordenada até a posição p - 1,
		incluímos o elemento p na lista, tornando-a ordenada até
		a posição p
	"""
	aux = l[p]
	i = p - 1
	while i >= 0 and aux < l[i]:
		l[i + 1] = l[i]
		i -= 1
	l[i + 1] = aux


def insertion_sort(l):
	"""
		Ordena uma lista de forma crescente
	"""
	for i in range(1, len(l)):
		inserir(l, i)


def merge(l1, l2):
  """
    Dadas duas listas ordenadas, junta as duas em uma lista ordenada
  """
  resultado = []
  i = 0
  j = 0

  # Preenchendo a lista em ordem crescente
  while i < len(l1) and j < len(l2):
    if l1[i] < l2[j]:
      resultado.append(l1[i])
      i += 1
    else:
      resultado.append(l2[j])
      j += 1

  # Adicionando os números que sobraram
  resultado += l1[i:]
  resultado += l2[j:]

  return resultado


def _merge_sort(l, inicio, fim):
  """
    Dada uma lista, ordena ela da posição inicio até fim
  """
  if fim - inicio <= 1: # Lista com 1 elemento ou menos já está ordenada
    return

  metade = (inicio + fim) // 2

  _merge_sort(l, inicio, metade)
  _merge_sort(l, metade, fim)

  l1 = l[inicio:metade]
  l2 = l[metade:fim]

  l[inicio:fim] = merge(l1, l2)


def merge_sort(l):
	"""
		Dada uma lista, ordena ela da posição inicio até fim
	"""
	_merge_sort(l, 0, len(l))


def partition(lista, inicio, fim):
  """
    Utiliza o primeiro elemento da lista como pivô, modificando lista de modo 
    que todos os elementos menores que pivô aparecem antes de pivô e todos os 
    elementos maiores aparecem depois. Retorna a nova posição do pivô
  """
  j = inicio # Posição do pivô

  for i in range(inicio + 1, fim):
    if lista[i] <= lista[inicio]: # Se menor que pivô
      j += 1
      trocar_elementos(lista, i, j)
  trocar_elementos(lista, inicio, j) # Coloque pivô após números menores
  return j


def _quick_sort(lista, inicio, fim):
  """
    Dada uma lista, ordena ela da posição inicio até fim
  """
  if inicio >= fim:
    return

  pivo = partition(lista, inicio, fim)
  _quick_sort(lista, inicio, pivo)
  _quick_sort(lista, pivo + 1, fim)


def quick_sort(lista):
  """
    Dada uma lista, ordena ela da posição inicio até fim
  """
  _quick_sort(lista, 0, len(lista))
