def palindromo(texto: str):
    texto_palindrom = texto[::-1]
    if(texto == texto_palindrom):
        print("É palindromo")
    else:
        print("Não é palindromo")

palindromo("python")