import pandas as pd

s = pd.Series([10,20,30,40,50])

dados = {
    "nome": ["Ana","Bruno","Carlos","Nicollas"],
    "idade": [22,32,69,19],
    "nota": [5.9,8.3,4.6,10.0]
}

df = pd.DataFrame(dados)

aprovado = df[df["nota"] > 8]

jovens = df[df["idade"] < 30]

df_dec = df.sort_values(by="nota", ascending=False)

df["situacao"] = ["Aprovado" if nota >= 7 else "Reprovado"

for nota in df["nota"]]

print(f"Series: \n{s}")

print(f"\nDataFrame: \n{df}")

print(f"\nPrimeira duas linhas:\n{df.head(2)}")

print(f"\nApenas a ultima linha:\n{df.tail(1)}")

print("\nMédia das Idades: \n", df["idade"].mean())

print("\nNota máxima: \n", df["nota"].max())

print("\nMenor nota: \n", df["nota"].min())

print("\n Visão geral do DataFrame: \n", df.describe())

print("Alunos Aprovado: \n", aprovado)

print("Alunos jovens: \n", jovens)

print("\Dataframe atualizado: \n", df)

print("Ordem decrescente: \n", df_dec)