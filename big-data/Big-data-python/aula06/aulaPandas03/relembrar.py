import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

s = pd.Series([10,20,30], index=["a","b","c"])
print(s)

dados = {
    "Nome": ["Ana","Bruno","Carlos"],
    "Idade": ["22","35","38"],
    "Curso": ["ADS","CP","Redes"]
}

df = pd.DataFrame(dados)

print(df)
