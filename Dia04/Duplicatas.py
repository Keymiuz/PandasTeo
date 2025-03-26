
# %%
import pandas as pd

import pandas as pd

df = pd.DataFrame({
    "nome": ['teo', 'lara', 'nah', 'bia', 'mah', 'lara', 'mah', 'mah'],
    "sobrenome": ['calvo', 'calvo', 'ataide', 'ataide', 'silva', 'silva', 'silva', 'silva'],
    "salario": [2132, 1231, 454, 6543, 6532, 4322, 987, 2134]
})

df
# %%
df = df.sort_values("salario", ascending=True) ## ordena o dataframe por salario em ordem crescente 
df

# %%

df.drop_duplicates(keep='first', subset=["nome", "sobrenome"]) ## remove duplicatas de nome e sobrenome 
df

# %%
df.drop_duplicates() # remove duplicatas de todas as colunas 
# %%
df.drop_duplicates(keep="last")
# %%
df.drop_duplicates(keep="first")
#

# %%
