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