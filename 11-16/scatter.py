import matplotlib.pyplot as plt
import geradores


xs, ys = geradores.gerar_scatter()

plt.scatter(xs, ys)
plt.show()