def num(num: int):
    if num % 2 == 0:
        return f"{num} é numero par"
    else:
        return f"{num} é numero impar"

resultado = num(10);

print(f"Resultado: {resultado}")

