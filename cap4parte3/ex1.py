import numpy as np

# carregando o dataset space.csv
dataset = np.loadtxt("space.csv", delimiter=";", dtype=str, encoding="utf-8")

# Filtrando as missões que deram certo
missoes_sucesso = dataset[dataset[:,-1] == "Success"]

# Calculando a porcentagem de missões que deram certo
porcentagem_sucesso = (len(missoes_sucesso) / len(dataset)) * 100

# Exibindo a porcentagem de missões que deram certo
print(f"Porcentagem de missões que deram certo: {porcentagem_sucesso:.2f}%")