def maior_numero_list(lista: list):
    maiorNumero = lista[0]
    segundoMaiorNumero = lista[0]
    for numero in lista:
        if(numero > maiorNumero):
            maiorNumero = numero
    print(maiorNumero)



lista_numeros = [10,20,30,40,50]

maior_numero_list(lista_numeros)
