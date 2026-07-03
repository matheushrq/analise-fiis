from leitura_dados import ler_csv
from tratamento import cria_carteira, filtra_dados, monta_carteira

def main():
    df = ler_csv()
    df_filtrado = filtra_dados(df)
    df_carteira = cria_carteira(df_filtrado)
    carteira_final = monta_carteira(df_carteira, n=10)
    print(carteira_final)

if __name__ == "__main__":
    main()