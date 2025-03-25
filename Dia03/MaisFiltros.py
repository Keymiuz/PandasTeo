# %%
import pandas as pd
df = pd.read_csv('../Data/transacao_produto.csv')
df.head()
# %%

filtro = (df["idProduto"] == 5) | (df["idProduto"] == 11)
df[filtro]

# %%
df["idProduto"].isin([5, 11])
# %%
filtro = df["idProduto"].isin([5, 11])
df[filtro] # Retorna um dataframe com os valores que atendem ao filtro 
##mesma coisa de cima, mas de um jeito mais enxuto
# %%

clientes = pd.read_csv("../data/clientes.csv")
clientes.head()


# %%
filtro = clientes["dtCriacao"].notna()
clientes[filtro]

# %%

clientes["dtCriacao"].isna()

# %%
clientes["dtCriacao"].notna()
# %%
clientes["dtCriacao"].isna()
~clientes["dtCriacao"].isna() # Retorna um df com valores inversos pelo ~
# %%
