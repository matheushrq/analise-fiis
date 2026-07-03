import pandas as pd

def ler_csv():
    df = pd.read_csv('dados/df_fiis_filtrados.csv', index_col='TICKER')
    return df