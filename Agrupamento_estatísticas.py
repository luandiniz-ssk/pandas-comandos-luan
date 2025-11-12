# Agrupar e somar
df.groupby("categoria")["vendas"].sum()

# Média por grupo
df.groupby("regiao")["preco"].mean()

# Contagem de valores únicos
df["cidade"].value_counts()
