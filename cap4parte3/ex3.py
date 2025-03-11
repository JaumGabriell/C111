import numpy as np

# Carregando o dataset space.csv
dataset = np.loadtxt("space.csv", delimiter=";", dtype=str, encoding="utf-8")

# Filtrando as missões dos EUA (terceira coluna, índice 2), verificando se "USA" está contido na string
missoes_EUA = dataset[np.char.find(np.char.upper(dataset[:, 2]), "USA") != -1]

# Calculando a quantidade de missões dos EUA
quantidade_missoes_EUA = len(missoes_EUA)

# Exibindo a quantidade de missões dos EUA
print("Quantidade de missões dos EUA: ", quantidade_missoes_EUA)