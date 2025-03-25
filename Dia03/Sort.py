
# %%

import pandas as pd

# %%

clientes = pd.read_csv("../data/clientes.csv")

max_ponto = clientes["qtdePontos"].max()
filtro = clientes["qtdePontos"] == max_ponto
clientes[filtro]

# %%

(clientes.sort_values(by="qtdePontos", ascending=False)
 .head(5)["idCliente"])

 # %%

 #você também pode usar o sort em listas e series e colocar ele como ascending e inserir o value em [] para facilitar sua vida