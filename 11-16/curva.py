import matplotlib.pyplot as plt
import geradores


xs, ys = geradores.gerar_reta()


plt.plot(xs, ys)
plt.show()