# %%
import pandas as pd
import os

df = pd.read_csv('../Data/clientes.csv')
df


# %%

df.to_csv('../Data/clientes.csv', index=False)
# %%

df.to_parquet('../Data/clientes.parquet', index=False)

# %%

df.to_excel('../Data/clientes.xlsx', index=False)

# %%
