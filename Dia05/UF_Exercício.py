# %%
import pandas as pd

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
dfs = pd.read_html(url)
# %%
df_ufs = dfs[1]
df_ufs
# %%
def str_to_float(x:str):
    x = float(x.replace(",", "")
               .replace(".", "")
               .replace("\xa0", "")) # esse xa0 foi um caracter especial que apareceu na primeira linha, só apareceu 1x
    return float(x)

# %%

df_ufs["Área (km²)"].apply(str_to_float)
# %%
df_ufs["Área (km²)"] = df_ufs["Área (km²)"].apply(str_to_float)
df_ufs["População (Censo 2022)"] = df_ufs["População (Censo 2022)"].apply(str_to_float)
df_ufs["PIB (2015)"] = df_ufs["PIB (2015)"].apply(str_to_float)
df_ufs["PIB per capita (R$) (2015)"] = df_ufs["PIB per capita (R$) (2015)"].apply(str_to_float)
df_ufs # sempre se lembrar de rodar a célula do DF primeiro dnv, se não vai dar erro
# %%
df_ufs.dtypes
# %%

# comparação de colunas agora >>

# Se PIB / Capita > 30.000
# +
# Mort Infantil < 15 / 1000
# +
# IDH (2010) > 700
# -> "Parece bom"

# Else, Não parece bom

def mortalidade_to_float(x:str):
    x = float(x.replace("%", "")
                .replace("‰", "")
                .replace(",", "."))
    return (x) / 1000

df_ufs["Mortalidade infantil (2016)"] = df_ufs["Mortalidade infantil (2016)"].apply(mortalidade_to_float)

# %%
# comparação de colunas agora >>

# Se PIB / Capita > 30.000
# +
# Mort Infantil < 15 / 1000
# +
# IDH (2010) > 700
# -> "Parece bom"

# Else, Não parece bom

def classifica_bom(linha):
    return (linha["PIB per capita (R$) (2015)"] > 30000 and
            linha["Mortalidade infantil (2016)"] < 15 and
            linha["IDH (2010)"] > 700)

df_ufs.apply(classifica_bom, axis=1)

# %%
# Cria uma nova coluna com os resultados da classificação
df_ufs["Parece bom"] = df_ufs.apply(classifica_bom, axis=1)

df_boas_ufs = df_ufs[df_ufs["Parece bom"]]# cria um novo DataFrame apenas com as linhas que são True



df_boas_ufs