import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")

df.head()

print(df.info())
print(df.isnull().sum())

print(df.drop(columns=["deck", "embark_town"], inplace=True))

print(df["age"].fillna(df["age"].mean()))

print(df.rename(columns={"sex": "Sexo", "age": "Idade"}, inplace=True))

df["class"].value_counts().plot(kind="bar", title="Distribuicao por Classe")
plt.show()

df["Idade"].plot(kind="hist", bins=20, color="skyblue", edgecolor="black")   
plt.title("Distribuicao de idades")
plt.xlabel("Idade")
plt.show()

sns.boxplot(x="class", y="fare", data=df)
plt.title("Distribuicao de tarifa por classe")
plt.show()

sns.scatterplot(x="age",y="fare", hue="sex",data=df)
plt.title("Idade x tarifa")
plt.show()

sns.scatterplot(x="Idade", y="fare", hue="Sexo", data=df)
plt.title("Idade x Tarifa")
plt.show()