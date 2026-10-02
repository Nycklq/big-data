import pandas as pd
vendas = pd.read_excel("aula04/excelpy/vendas.xlsx")

print(vendas)

print("Dimensoes da planilha: ")
print(vendas.shape)

print("Apenas as duas primeiras linhas: ")
print(vendas.head(2))

## vendas_janeiro = pd.read_excel("aula04/excelpy/vendas.xlsx", sheet_name="Janeiro")

##print(vendas_janeiro) fiz pra testar so nao vai funcionar pq nao coloquei o mes no excel