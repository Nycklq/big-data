import numpy as np

lista_num = np.array([1, 2, 3, 4, 5, 6])

a = np.array([1,2,3])

b = np.array([[1,2,3], [4,5,6]])

zeros = np.zeros((2,3))

ones = np.ones((3,3))

seq = np.arange(0,10,2)

linspace = np.linspace(0,1,5);

x = np.array([1,2,3,4,5])
y = np.array([10,20,30,40,50])

lista_notas = np.array([9.1,3.5,9.8,6.4,7.8])

def mostraValores():
    print("Array: ", lista_num)
    print("Tipo: ", type(lista_num))
    print("Dimensao: ", lista_num.ndim)
    print("Tamanho: ", lista_num.size)
    print("A: ", a)
    print("B: ", b)
    print("Zeros: ", zeros)
    print("Ones: ", ones)
    print("Seq: ", seq)
    print("Linspace: ", linspace)
    print("X: ", x)
    print("Y: ", y)
    print("Soma", x + y)
    print("Mult", x * y)
    print("Quadrado", x ** y)
    print("Seno: ", np.sin(x))
    print("Media: ", np.mean)
    print("Desvio padrao: ", np.std(x))
    print("Máximo: ", lista_notas.max())
    print("Mínimo: ", lista_notas.min())
    print("Média: ", lista_notas.mean())
    print("Posição da menor nota: ", lista_notas.argmin())
