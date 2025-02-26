import numpy as np

# Define a seed para gerar números aleatórios
np.random.seed(10)

# Cria uma matriz 4x4 com números aleatórios inteiros entre 1 e 50
matriz = np.random.randint(1, 51, size=(4, 4))

# Calcula a média de cada linha
media_linhas = np.mean(matriz, axis=1)

# Calcula a média de cada coluna
media_colunas = np.mean(matriz, axis=0)

# Encontra o maior valor das médias das linhas e das colunas
maior_media_linhas = np.max(media_linhas)
maior_media_colunas = np.max(media_colunas)

# Conta as aparições de cada número na matriz
contagem = np.bincount(matriz.flatten())

# Encontra os números que aparecem exatamente 2 vezes
numeros_2_vezes = np.where(contagem == 2)[0]

# Mostra a matriz
print("Matriz 4x4:")
print(matriz)

# Mostra a média de cada linha
print("\nMédia de cada linha:")
for i, media in enumerate(media_linhas):
    print(f"Linha {i+1}: {media:.2f}")

# Mostra a média de cada coluna
print("\nMédia de cada coluna:")
for i, media in enumerate(media_colunas):
    print(f"Coluna {i+1}: {media:.2f}")

# Mostra o maior valor das médias das linhas e das colunas
print(f"\nMaior média das linhas: {maior_media_linhas:.2f}")
print(f"Maior média das colunas: {maior_media_colunas:.2f}")

# Mostra a quantidade de aparições de cada número na matriz
print("\nQuantidade de aparições de cada número na matriz:")
for numero, quantidade in enumerate(contagem):
    if quantidade > 0:
        print(f"Número {numero}: {quantidade} vez(es)")

# Mostra os números que aparecem exatamente 2 vezes
print("\nNúmeros que aparecem exatamente 2 vezes:")
for numero in numeros_2_vezes:
    print(numero)