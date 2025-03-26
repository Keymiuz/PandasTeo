# %%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv")
clientes.head()
# %%

clientes.dropna()
# %%

clientes.dropna(how="any")

# %%

df = pd.DataFrame({
    "nome": ["Téo", None, "Nah", "Marcio"],
    "idade": [None, None, 43, 52],
    "salario": [3453, 4324, None, 5423]
})

df
# %%
df.dropna(how="any", subset=["idade", "salario"])
# %%
df.dropna(how="all", subset=["idade", "nome"])
# %%
df["idade"].fillna(0, inplace=True) ## coloquei o inplace para visualizar o dataframe
df
# %%
df["nome"].fillna("Xerath", inplace=True) # mesma lógica do de cima
df
# %%
