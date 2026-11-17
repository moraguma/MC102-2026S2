import matplotlib.pyplot as plt
import geradores


xs, ys = geradores.gerar_barras()


plt.bar(xs, ys)
plt.show()