# %%
import pandas as pd

# %%
transações = pd.read_csv('../Data/transacoes.csv')
transações.head()


# %%
transações.groupby(by="idCliente").count()
# %%
transações.groupby(by=["idCliente"], as_index=False)[["idTransacao"]].count() # duas chaves no "idTransação para retornar um DF e as_index=False para não criar um index com o idCliente
# %%
summary = (transações.groupby(by=["idCliente"], as_index=False)
                      .agg({
                          "idTransacao": ["count"],
                          "qtdePontos": ["sum", "mean"]
                      }))

summary
# %%
