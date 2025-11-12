# Nova coluna baseada em outra
df["dobro"] = df["valor"] * 2

# Condicional
df["status"] = df["idade"].apply(lambda x: "Adulto" if x >= 18 else "Menor")

# Remover coluna
df.drop("coluna", axis=1, inplace=True)
