import math

numero = float(input("Digite um número decimal: "))

raiz_quadrada = math.sqrt(numero)
teto = math.ceil(numero)
chao = math.floor(numero)
parte_inteira = int(numero)

print(f"Raiz quadrada: {raiz_quadrada}")
print(f"Função teto: {teto}")
print(f"Função chão: {chao}")
print(f"Parte inteira: {parte_inteira}")