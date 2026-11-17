import matplotlib.pyplot as plt
import geradores

# Fig <- Figura
# Axes <- Eixos 
fig, axes = plt.subplots(
    2,
    2,
    figsize=(16,8)
)


for i in range(2):
    for j in range(2):
        xs, ys = geradores.gerar_reta()

        axes[i][j].plot(xs, ys)
fig.savefig("11-16/fig.png")