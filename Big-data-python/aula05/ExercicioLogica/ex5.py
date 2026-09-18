def somaNumeros(num: int):
    soma = 0
    for i in range(1, num + 1):
        soma = soma + i
    print(f"Soma dos numeros é {soma}")

somaNumeros(5) 