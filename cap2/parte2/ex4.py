n = int(input('Qual a distância em km? '))

if n <= 200:
    print(f'Preço: {n * 0.5}')
else:
    print(f'Preço: {n * 0.45}')