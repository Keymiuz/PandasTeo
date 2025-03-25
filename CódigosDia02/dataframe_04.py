# %%
import pandas as pd  

df_cliente = pd.read_csv('../Data/clientes.csv')
df_cliente

# %%
df_cliente.info()
df_cliente.head(n=10) # amostra inicial
# %%
df_cliente.tail(n=10) # amostra final
# %%
df_cliente.sample(n=30) # amostra aleatória
# %%
df_cliente.columns # colunas
# %%
df_cliente.dtypes # tipos de dados
# %%
df_cliente.isnull().sum() # valores nulos
# %%
df_cliente.describe() # estatísticas

# %%
df_cliente.shape # dimensões
# %%
df_cliente.index # indices
# %%
df_cliente.dtypes["dtCriacao"] # tipos de dados (é possível navegar nesses valores já que é uma série)
# %%
df_cliente.dtypes["dtAtualizacao"]
# %%
df_cliente.dtypes["flEmail"]
# %%
df_cliente.dtypes["idCliente"]
# %%
df_cliente.dtypes["flYouTube"]

# %%
 