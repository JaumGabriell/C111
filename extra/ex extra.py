import numpy as np

# Carregando o dataset paises.csv
dataset = np.genfromtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8', skip_header=1, invalid_raise=False, filling_values='')

# Removendo espaços extras das strings no dataset
dataset = np.char.strip(dataset)

# Verificando a forma do dataset para garantir que é 2-dimensional
print("Forma do dataset:", dataset.shape)

# Verificando as primeiras linhas do dataset para garantir que foi carregado corretamente
print("Primeiras linhas do dataset:")
print(dataset[:5])

# Exercício 1
country_idx = 0
region_idx = 1
population_idx = 2
area_idx = 3

# Fazendo o slicing para selecionar apenas as colunas desejadas
if dataset.ndim == 2:
    selected_columns = dataset[:, [country_idx, region_idx, population_idx, area_idx]]

    # Exibindo as informações das colunas selecionadas
    print("\nPaís, Região, População e Área dos países:")
    for row in selected_columns:
        print(f"País: {row[0]}, Região: {row[1]}, População: {row[2]}, Área: {row[3]}")
else:
    print("O dataset não é 2-dimensional. Verifique o arquivo CSV.")

# ====================================================================================================

# Exercício 2

# Selecionando a coluna de regiões
if dataset.ndim == 2:
    regioes = dataset[:, region_idx]

    # Contando as diferentes regiões
    diferentes_regioes = np.unique(regioes)

    # Exibindo as diferentes regiões
    print("\nDiferentes regiões do planeta segundo o dataset:")
    for regiao in diferentes_regioes:
        print(regiao)
else:
    print("O dataset não é 2-dimensional. Verifique o arquivo CSV.")

# ====================================================================================================

# Exercício 3

# Índice da coluna de alfabetização (Literacy (%), coluna J)
literacy_idx = 9

# Selecionando a coluna de alfabetização
if dataset.ndim == 2:
    literacy_rates = dataset[:, literacy_idx]

    # Convertendo os valores para float, ignorando valores não numéricos
    literacy_rates_float = []
    for rate in literacy_rates:
        try:
            literacy_rates_float.append(float(rate))
        except ValueError:
            continue

    # Calculando a média dos valores
    literacy_mean = np.mean(literacy_rates_float)

    # Exibindo a taxa média de alfabetização
    print(f"\nTaxa média de alfabetização do planeta: {literacy_mean:.2f}%")
else:
    print("O dataset não é 2-dimensional. Verifique o arquivo CSV.")

# ====================================================================================================

# Exercício 4

# Contando quantos países são da América do Norte (NORTHERN AMERICA)
if dataset.ndim == 2:
    northern_america_count = np.sum(regioes == 'NORTHERN AMERICA')

    # Exibindo a quantidade de países da América do Norte
    print(f"\nQuantidade de países da América do Norte (NORTHERN AMERICA): {northern_america_count}")
else:
    print("O dataset não é 2-dimensional. Verifique o arquivo CSV.")

# ====================================================================================================

# Exercício 5

# Índice da coluna de renda per capita (GDP ($ per capita), coluna I)
gdp_idx = 8

# Selecionando as colunas de região e renda per capita
if dataset.ndim == 2:
    regioes = dataset[:, region_idx]
    gdp_per_capita = dataset[:, gdp_idx]
    paises = dataset[:, country_idx]

    # Filtrando os países da região "LATIN AMER. & CARIB"
    latin_america_carib_filter = regioes == 'LATIN AMER. & CARIB'
    latin_america_carib_gdp = gdp_per_capita[latin_america_carib_filter]
    latin_america_carib_paises = paises[latin_america_carib_filter]

    # Convertendo os valores de renda per capita para float, ignorando valores não numéricos
    latin_america_carib_gdp_float = []
    latin_america_carib_paises_validos = []
    for i, gdp in enumerate(latin_america_carib_gdp):
        try:
            latin_america_carib_gdp_float.append(float(gdp))
            latin_america_carib_paises_validos.append(latin_america_carib_paises[i])
        except ValueError:
            continue

    # Verificando se a lista não está vazia antes de encontrar o índice do país com a maior renda per capita
    if latin_america_carib_gdp_float:
        # Encontrando o índice do país com a maior renda per capita
        indice_maior_gdp = np.argmax(latin_america_carib_gdp_float)

        # Obtendo o país com a maior renda per capita
        pais_maior_gdp = latin_america_carib_paises_validos[indice_maior_gdp]
        maior_gdp = latin_america_carib_gdp_float[indice_maior_gdp]

        # Exibindo o país com a maior renda per capita
        print(f"\nPaís da América do Sul e Caribe (LATIN AMER. & CARIB) com a maior renda per capita: {pais_maior_gdp}")
        print(f"Renda per capita: {maior_gdp}")
    else:
        print("Não há dados válidos de renda per capita para a região 'LATIN AMER. & CARIB'.")
else:
    print("O dataset não é 2-dimensional. Verifique o arquivo CSV.")