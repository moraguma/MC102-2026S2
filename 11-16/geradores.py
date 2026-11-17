import numpy as np


def mostrar_dados(msg, dados):
  """
    Imprime dados representados por um objeto iterável
  """
  print(f"Formato de {msg} - {dados.shape}")


def gerar_ruido(dados, m=0.1, dp=0.1):
  """
    Gera uma quantidade de ruído para adicionar em uma série de dados
  """
  return np.random.normal(m, dp, dados.shape)


def gerar_reta():
  """
    Gera uma reta de angulação aleatória
  """
  m = np.random.uniform(-1.0, 1.0)
  b = np.random.uniform(-1.0, 1.0)
  xs = np.arange(0.0, 1.0, 0.01)

  ys = xs * m + b
  ys += gerar_ruido(ys)

  mostrar_dados("x", xs)
  mostrar_dados("y", ys)
  return xs, ys


def gerar_barras():
  """
    Gera um gráfico de barra com valores em distribuição normal
  """
  xs = np.array(["A", "B", "C", "D", "E"])

  ys = np.zeros(xs.shape)
  ys += gerar_ruido(ys)

  mostrar_dados("x", xs)
  mostrar_dados("y", ys)
  return xs, ys


def gerar_scatter():
  """
    Gera uma nuvem de pontos centrada em (0, 0)
  """
  xs = np.zeros(1000)
  xs += gerar_ruido(xs)

  ys = np.zeros(1000)
  ys += gerar_ruido(ys)

  mostrar_dados("x", xs)
  mostrar_dados("y", ys)
  return xs, ys


def gerar_matriz():
  """
    Gera uma matriz de pontos em uma distribuição gaussiana centrada em (0.0, 0.0)
  """
  n = 100

  x = np.linspace(-1.0, 1.0, n)
  xs, ys = np.meshgrid(x, x)

  sigma = 0.3
  means = np.exp(-(xs**2 + ys**2) / (2 * sigma**2))

  rng = np.random.default_rng()
  matriz = rng.normal(loc=means, scale=0.1)

  mostrar_dados("Matriz", matriz)
  return matriz
