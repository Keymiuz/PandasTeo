# %%
from numpy import True_
import pandas as pd

df = pd.read_csv('../Data/clientes.csv')
df.head()

# %%

df["qtdePontos"] + 100
# %%
nova_coluna = []
for i in df["qtdePontos"]:
    nova_coluna.append(i + 100)

nova_coluna ## metodo com laço for, bem mais custoso de memoria e também bem mais trabalhoso de se escrever kkkk


# %%

df["pontos_100"] = df["qtdePontos"] + 100
df.head()

# %%

nova_coluna = []
for i in df["qtdePontos"]:
    nova_coluna.append(i + 100)

nova_coluna

# %%

df["emailtwitch"] = df["flEmail"] + df["flTwitch"] #concatenando colunas de mesma dimensão
df.head()
# %%
df["qtSocial"] = df["flEmail"] + df["flTwitch"] + df["flBlueSky"] + df["flYouTube"] + df["flInstagram"] #concatenando colunas de mesma dimensão
df.head()
# %%
import matplotlib.pyplot as plt
plt.grid(True)

plt.show() # cria o grafico
plt.hist(df["qtSocial"]) # histograma
# %%

