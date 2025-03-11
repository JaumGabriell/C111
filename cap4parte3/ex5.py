import numpy as np

# Carregando o dataset space.csv
dataset = np.loadtxt("space.csv", delimiter=";", dtype=str, encoding="utf-8")

# Dicionário para armazenar a contagem de missões por empresa
contagem_missoes = {}

# Iterando sobre as linhas do dataset
for linha in dataset:
    empresa = linha[1]  # Nome da empresa (segundo índice, índice 1)
    if empresa in contagem_missoes:
        contagem_missoes[empresa] += 1
    else:
        contagem_missoes[empresa] = 1

# Mostrando o nome das empresas e suas respectivas quantidades de missões
print("Nome das empresas e suas respectivas quantidades de missões:")
for empresa, quantidade in contagem_missoes.items():
    print(f"{empresa}: {quantidade} missões")