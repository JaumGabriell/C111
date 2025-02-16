serieA = ['botafogo', 'flamengo', 'vasco', 'Barcelona', 'santos']

print("Os 3 primeiros colocados:")
for i in range(3):
    print(f'{i+1}º colocado: {serieA[i]}')

print("\nOs últimos 2 colocados:")
for i in range(2):
    print(f'{len(serieA)-i}º colocado: {serieA[-(i+1)]}')

serieA_ordenada = sorted(serieA)
print("\nTimes em ordem alfabética:")
for time in serieA_ordenada:
    print(time)

posicao_barcelona = serieA.index('Barcelona') + 1
print(f'\nBarcelona está na {posicao_barcelona}ª posição')