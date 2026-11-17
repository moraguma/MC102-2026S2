import matplotlib.pyplot as plt
import geradores

plt.style.use('_mpl-gallery')


xs, ys = geradores.gerar_reta()


plt.plot(xs, ys)
plt.grid()
plt.show()