import numpy as np

matriz = np.arange(1,17).reshape(4,4)

print("Matriz 4 x 4: ", matriz)
print("Soma: ", matriz.sum())
print("Média: ", matriz.mean())
print("Primeira coluna: ",matriz[: , 0])
print("Ultimo elemento: ",matriz[-1 , -1])
