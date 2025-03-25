
# %%
import pandas as pd

df = pd.read_csv("../Data/transacoes.csv")
df
# %%
colunas = ["idCliente", "qtdePontos"]
df[colunas]

# %%
# SELECT * FROM df
df

# %%
# SELECT idCliente FROM df
df[['idCliente']]

# %%
# SELECT idCliente, qtPontos FROM df LIMIT 5
df[['idCliente', 'qtdePontos']].head(5)  #a ordem sempre vem conforme eu escrevo ela
# %%
colunas = list(df.columns) # colunas do dataframe 
colunas.sort() # ordenar colunas 
colunas

df = df[colunas] # reordenar colunas 
df
# %%
