# Selecionar a primeira transação DIARIA de cada cliente


# %%

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv")
transacoes.head()
# %%

transacoes = transacoes.sort_values("dtCriacao")
transacoes["Dia"] = pd.to_datetime(transacoes["dtCriacao"]).dt.date
transacoes
## mas e agora, como eu pego a primeira do dia ???
# %%
first = transacoes.drop_duplicates(subset=["idCliente", "Dia"], keep="first")
first


# %%
last = transacoes.drop_duplicates(subset=["idCliente", "Dia"], keep="last")
last
# %%
pd.concat([first, last]) # concatena os dois dataframes (como se fosse um join)
# %%
