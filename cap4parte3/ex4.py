import numpy as np

# Carregando o dataset space.csv
dataset = np.loadtxt("space.csv", delimiter=";", dtype=str, encoding="utf-8")

# Filtrando as missões realizadas pela empresa "SpaceX" (segundo índice, índice 1)
missoes_spacex = dataset[np.char.strip(np.char.upper(dataset[:, 1])) == "SPACEX"]

# Convertendo a penúltima coluna (custo) para float, ignorando valores não numéricos
custos = []
missoes_validas = []
for i, valor in enumerate(missoes_spacex[:, -2]):
    try:
        custo = float(valor)
        custos.append(custo)
        missoes_validas.append(missoes_spacex[i])
    except ValueError:
        continue

# Convertendo a lista de custos para um array numpy
custos = np.array(custos)

# Encontrando o índice da missão mais cara
indice_missao_mais_cara = np.argmax(custos)

# Obtendo a missão mais cara
missao_mais_cara = missoes_validas[indice_missao_mais_cara]

# Exibindo a missão mais cara
print("Missão mais cara realizada pela SpaceX:")
print(f"Nome da missão: {missao_mais_cara[0]}")
print(f"Custo: {missao_mais_cara[-2]}")