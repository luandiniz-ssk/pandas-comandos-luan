# Remover linhas nulas
df.dropna(inplace=True)

# Preencher valores nulos com média
df["coluna"] = df["coluna"].fillna(df["coluna"].mean())

# Remover duplicatas
df.drop_duplicates(inplace=True)

# Converter tipos
df["data"] = pd.to_datetime(df["data"])
df["valor"] = df["valor"].astype(float)

# Renomear colunas
df.rename(columns={"Nome Antigo": "novo_nome"}, inplace=True)

