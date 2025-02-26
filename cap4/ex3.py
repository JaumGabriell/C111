import numpy as np

arr1 = np.zeros(4)

aux = np.random.randint(0,4)

arr1[aux] = 1

mtz = arr1.reshape(2,2)

def posicao_para_indice(linha, coluna):
    return linha * 2 + coluna

# Variável para contar o número de jogadas
jogadas = 0

# Variável para controlar se o jogo terminou
game_over = False

# Solicita ao usuário que faça uma jogada
while jogadas < 3 and not game_over:
    print("\nMatriz 2x2:")
    print(mtz)
    linha = int(input("Digite a linha (0 ou 1): "))
    coluna = int(input("Digite a coluna (0 ou 1): "))
    indice = posicao_para_indice(linha, coluna)
    
    if arr1[indice] == 1:
        print("Game Over! :( Try Again!")
        game_over = True
    else:
        print("Posição vazia. Continue jogando.")
        jogadas += 1

if not game_over:
    print("Congratulations! You beat the game! :)")