import pandas as pd
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def contar_palavras(texto: str):
    palavras = re.findall(r"[w']+", texto.lower())
    series = pd.Series(palavras)
    contagem = series.value_counts()
    return contagem

if __name__ == "__main__":
    with open("aula05/teste.txt", "r", encoding="utf-8") as f:
        texto = f.read()
    resultado = contar_palavras(texto)
    print(resultado)

    nuvem = WordCloud(width=800,height=400,background_color="White").generate(texto)

    plt.figure(figsize=(10,5))
    plt.imshow(nuvem, interpolation="bilinear")
    plt.axis("off")
    plt.title("Nuvem de Palavras")
    plt.show()