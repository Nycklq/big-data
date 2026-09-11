import pandas as pd

dados = {
    "nomee": ["Ana", "Pedro", "Lucas"],
    "Idade": [23, 30, 25],
    "Cidade": ["SP", "RJ", "BH"]
}

df = pd.DataFrame(dados)

print(df)

print(df[df["Idade"]] > 24)