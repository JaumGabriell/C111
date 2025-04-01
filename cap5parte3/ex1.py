import pandas as pd

try:
    # Tente carregar o arquivo CSV com o delimitador correto
    df = pd.read_csv('paises.csv', delimiter=';', encoding='utf-8', on_bad_lines='skip')

    # 1.a. Quais são os países da OCEANIA
    paises_oceania = df[df['Region'].str.contains('OCEANIA', case=False, na=False)]
    print("Países da OCEANIA:")
    print(paises_oceania['Country'])

    # 1.b. Quantos países são da OCEANIA
    quantidade_oceania = paises_oceania.shape[0]
    print(f"\nQuantidade de países da OCEANIA: {quantidade_oceania}")

    # 2. País com a maior população
    pais_maior_populacao = df.loc[df['Population'].idxmax(), ['Country', 'Region']]
    print(f"\nPaís com a maior população: {pais_maior_populacao['Country']} ({pais_maior_populacao['Region']})")

    # 3. Média de alfabetização por região
    media_alfabetizacao = df.groupby('Region')['Literacy (%)'].mean()
    print("\nMédia de alfabetização por região:")
    print(media_alfabetizacao)

    # 4. Países sem costa marítima
    paises_sem_costa = df[df['Coastline (coast/area ratio)'] == 0]
    paises_sem_costa[['Country']].to_csv('noCoast.csv', index=False)
    print("\nArquivo 'noCoast.csv' criado com os países sem costa marítima.")

    # 5. Função para taxa de mortalidade e criação da nova coluna
    def humanitarian_help(deathrate):
        return 'Balanced' if deathrate < 9 else 'Urgent'

    df['Humanitarian Help'] = df['Deathrate'].apply(humanitarian_help)
    print("\nDataset com a nova coluna 'Humanitarian Help':")
    print(df)

except pd.errors.ParserError as e:
    print(f"Erro ao processar o arquivo CSV: {e}")
except FileNotFoundError:
    print("Arquivo 'paises.csv' não encontrado. Verifique o caminho e tente novamente.")