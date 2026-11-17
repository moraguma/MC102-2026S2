import matplotlib.pyplot as plt
import geradores


xs, ys = geradores.gerar_scatter()
plt.hist(xs, 10)
plt.show()