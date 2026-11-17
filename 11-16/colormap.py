import matplotlib.pyplot as plt
import geradores

fig, ax = plt.subplots(1, 1)

xs, ys = geradores.gerar_reta()

ax.set_xlim((-0.05, 1.05))
ax.set_ylim((-2.0, 2.0))
ax.scatter(xs, ys, c=-xs, cmap="cool")
fig.savefig("11-16/fig.png")