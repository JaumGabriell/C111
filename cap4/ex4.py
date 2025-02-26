import numpy as np

# Cria uma matriz de tamanho qualquer (por exemplo, 3x4)
matriz = np.random.randint(0, 10, size=(3, 4))

# Extrai o número de linhas e colunas
num_linhas, num_colunas = matriz.shape

# Multiplica o número de linhas e colunas
num_elementos = num_linhas * num_colunas

# Determina se o número de elementos é par ou ímpar
if num_elementos % 2 == 0:
    paridade = "par"
else:
    paridade = "ímpar"

# Mostra a matriz e a paridade do número de elementos
print("Matriz:")
print(matriz)
print(f"\nA matriz pode se tornar um vetor unidimensional com {num_elementos} elementos, que é um número {paridade}.")