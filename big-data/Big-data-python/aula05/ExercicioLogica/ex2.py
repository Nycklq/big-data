def maior_de_tres(num1: int, num2: int, num3: int):
    if(num1 > num2 and num1 > num3):
        print(f"{num1} é maior")
    elif (num2 > num1 and num2 > num3):
        print(f"{num2} é maior")
    else:
        print(f"{num3} é maior")

resultado = maior_de_tres(10,20,30)

