# %%
import pandas as pd

df = pd.read_csv('../Data/clientes.csv')
df.head()
# %%
idCliente = "ea0ff655-fa9f-4baa-a198-47f581ec52a1"

def get_last_id(x):
    return x.split("-")[-1] #criando uma mini função para pegar o último id do DF 

get_last_id(idCliente)
# %%
df["idCliente"] = df["idCliente"].apply(get_last_id)
df.head()
# %%
