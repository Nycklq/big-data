import numpy as np 

dados = np.random.randint(0, 51, 100)

contagem = np.bincount(dados)
moda = np.argmax(contagem)

print("Média: ", np.mean(dados))
print("Mediana: ", np.median(dados))
print("Desvio padrão: ", np.std(dados))
print("Moda: ", moda)
