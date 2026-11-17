import matplotlib.pyplot as plt
import geradores


fig, axes = plt.subplots(
    1, # Número de linhas
    2, # Número de colunas
    figsize=(8, 4)
)

xs1, ys1 = geradores.gerar_reta()
xs2, ys2 = geradores.gerar_reta()


axes[0].plot(xs1, ys1, "^-", c="#974E0A", label="Material 1")
axes[0].plot(xs2, ys2, "--", c="hotpink", label="Material 2")
axes[1].plot(xs1, ys1, label="Material 1")
axes[1].plot(xs2, ys2, label="Material 2")

axes[0].set_xlabel("Tempo (s)")
axes[0].set_ylabel("Temperatura (10³ °C)")
axes[0].set_title("Evolução da temperatura")

axes[0].set_xlim((-0.05, 1.05))
axes[0].set_ylim((-2.0, 2.0))

axes[0].legend()

fig.savefig("11-16/fig.png")