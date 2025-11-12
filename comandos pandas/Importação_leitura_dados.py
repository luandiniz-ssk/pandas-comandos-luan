
# 1 Importação e leitura de dados

import pandas as pd

# Ler arquivos
df = pd.read_csv("dados.csv")         # CSV
# df = pd.read_excel("planilha.xlsx") # Excel
# df = pd.read_json("dados.json")     # JSON

print(df.head())   # Mostra as 5 primeiras linhas



