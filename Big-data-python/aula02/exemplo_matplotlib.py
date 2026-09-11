import matplotlib.pyplot as plt

produtos = ["Notebook", "Mouse", "Teclado", "Monitor", "Headset"]
vendas = [30,120,80,62]

plt.bar(produtos, vendas)
plt.title("Vendas por Ano")
plt.xlabel("Ano")
plt.ylabel("Vendas")
plt.grid(True)
plt.show()