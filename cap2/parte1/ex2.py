n = int(input("Digite um número: "))

incio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

for i in range(incio, fim +1):
    print(n * i)