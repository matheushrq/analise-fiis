import pandas as pd
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import pdist, squareform
from leitura_dados import ler_csv

df = ler_csv()

# filtrando os dados para uma melhor análise
def filtra_dados(df):
    filtro_dy = df['MEDIA_YIELD_12M'] >= 0.8
    filtro_pvp = df['PVP'] <= 1
    filtro_cotista = df['NUMERO_COTISTA'] >= 100000

    mediana_liquidez = df['LIQUIDEZMEDIADIARIA'].median()
    filtro_liquidez = df['LIQUIDEZMEDIADIARIA'] >= mediana_liquidez

    df_filtrado = df[filtro_dy & filtro_pvp & filtro_cotista & filtro_liquidez]
    return df_filtrado

# composição da carteira
def cria_carteira(df_filtrado):
    # Seleção das variáveis relevantes
    # Atributos que descrevem cada fundo imobiliário
    # Características de cada fundo imobiliário
    variaveis = df_filtrado[['PVP', 'MEDIA_YIELD_12M', 'LIQUIDEZMEDIADIARIA']]

    # Padronização das variáveis
    # Cada variável tem escala diferente
    # Padronização é necessária para evitar que variáveis com maior escala dominem a análise
    df_normalizado = StandardScaler().fit_transform(variaveis)

    # Cálculo da matriz de distância
    # Distância euclidiana entre os fundos imobiliários
    # Matriz de distância é simétrica e tem zeros na diagonal
    matriz_distancia = squareform(pdist(df_normalizado, metric='euclidean'))
    pd.DataFrame(matriz_distancia, index=df_filtrado.index, columns=df_filtrado.index)

    diversidade_score = matriz_distancia.sum(axis=1)
    df_filtrado['diversidade_score'] = diversidade_score

    return df_filtrado

def monta_carteira(df_filtrado, n):
    carteira = df_filtrado.sort_values(by='diversidade_score', ascending=False).head(n)
    carteira.to_csv('final/carteira.csv')
    return carteira