import numpy as np

# Carregando o dataset space.csv, pulando a primeira linha (cabeçalho)
dataset = np.loadtxt("space.csv", delimiter=";", dtype=str, encoding="utf-8", skiprows=1)

# Convertendo a penúltima coluna para float, ignorando valores não numéricos
custos = []
for valor in dataset[:, -2]:
    try:
        custos.append(float(valor))
    except ValueError:
        continue

# Convertendo a lista para um array numpy
custos = np.array(custos)

# Filtrando os valores maiores que 0
custos_validos = custos[custos > 0]

# Calculando a média dos valores filtrados
media_gastos = np.mean(custos_validos)

# Exibindo a média de gastos
print(f"Média de gastos (considerando valores > 0): {media_gastos:.2f}")