# Selecionar colunas
df["coluna"]
df[["coluna1", "coluna2"]]

# Filtrar linhas
df[df["idade"] > 30]
df[(df["cidade"] == "São Paulo") & (df["idade"] > 25)]
