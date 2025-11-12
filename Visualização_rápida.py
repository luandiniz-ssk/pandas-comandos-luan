import matplotlib.pyplot as plt

df["vendas"].plot(kind="bar")
plt.title("Vendas por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Total de Vendas")
plt.show()
