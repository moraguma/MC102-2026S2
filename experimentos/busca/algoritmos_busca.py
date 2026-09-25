def busca_sequencial(l, x):
	"""
		Retorna a posição de x em l. Se x não está em l, retorna -1
	"""
	for i in range(len(l)):
		if l[i] == x:
			return i
	return -1


def busca_binaria(l, x):
	"""
		Retorna a posição de x em l. Se x não está em l, retorna -1. Assume
		que l está ordenada
	"""
	pos_ini = 0
	pos_fim = len(l) - 1

	while pos_ini <= pos_fim:
		pos_meio = (pos_ini + pos_fim) // 2
		if l[pos_meio] > x:
			pos_fim = pos_meio - 1
		elif l[pos_meio] < x:
			pos_ini = pos_meio + 1
		else:
			return pos_meio
	return -1