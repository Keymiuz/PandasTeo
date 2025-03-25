# %%
import pandas as pd

# %%
df = pd.read_csv('../Data/transacoes.csv')
df.head() 

# %%

pontos = [1, 2, 10 , 30, 100, 50, 25, 50, 30, 100, 104, 1000, 10000, 4000]
filtro = [i >= 50 for i in pontos]

for i in pontos:
    if i >= 50:
        filtro.append(i>=50)
filtro
# %%
resultado = []

for i in range (len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])

resultado
# %%
import pandas as pd 

df_brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "nah", "mah"],
        "idade": [32, 35, 14],
        "uf": ["sp", "pr", "rj"],
    }
)

pd.DataFrame(df_brinquedo)

filtro = df_brinquedo["idade"] >= 18 # Retorna uma série booleana 
filtro

df_brinquedo[filtro] # Retorna um dataframe com os valores que atendem ao filtro

## sempre tem a mesma quantidade de linhas que meu dataframe (ou a lista)

# %%
df = pd.read_csv('../Data/transacoes.csv')
df.head() # agora com exemplos reais
# %%
filtro = (df["qtdePontos"] >= 50) & (df["qtdePontos"] <= 100) ## operador "e"
df[filtro]

# %%
filtro = (df["qtdePontos"] >= 50) | (df["qtdePontos"] <= 100) ## operador "ou"
df[filtro]

# %%
# pontos entre 0 e 50 ou do ano de 2025 para frente
filtro = ((df["qtdePontos"] > 0) & (df["qtdePontos"] <= 50)) | (df["dtCriacao"] >= '2025-01-01')
df[filtro]
# %%
