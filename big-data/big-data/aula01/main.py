def retangulo(b: float, a: float) -> float:
    return b * a

def quadrado(x):
    return x ** 2

retangulo = retangulo(10,2)

quadrado = quadrado(10)

def dolar(valor):
    dolar = 5.19
    return valor * dolar

def real(valor):
    return valor / 5.19

dolar = dolar(10)

real = real(2)

print(f"retangulo: {retangulo:.2f}")

print(f"quadrado: {quadrado:.2f}")

print(f"Real: {real:.2f}")

print(f"Dolar: {dolar:.2f}")