import matplotlib.pyplot as plt
import geradores


xs, ys = geradores.gerar_scatter()

plt.hist2d(xs, ys, [20, 20], cmap="hot")
plt.colorbar()
plt.show()