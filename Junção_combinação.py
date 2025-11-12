# Juntar dois DataFrames
df_final = pd.merge(df1, df2, on="id", how="inner")
# how pode ser: 'inner', 'left', 'right', 'outer'
