# %%
import pandas as pd
import numpy as np

# %%
transações = pd.read_csv('../Data/transacoes.csv')
transações.head()

# %%
def diff_amp(x: pd.Series):
    amplitude = x.max() - x.min()
    media = x.mean()
    return np.sqrt((amplitude - media)**2)

idades = pd.Series([21, 32, 43, 32, 14, 65, 78, 34, 19])

diff_amp(idades)


# %%
transações.groupby(by=["idCliente"]).agg({
    "idTransacao": ["count"],
    "qtdePontos": ["sum", "mean", diff_amp] 
})
# %%
