pessoas = []

n = int(input("Digite o número de pessoas: "))

for i in range(n):
    nome = input(f"Digite o nome da pessoa {i+1}: ")
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    sexo = input(f"Digite o sexo da pessoa {i+1} (M/F): ").strip().upper()
    pessoas.append({'nome': nome, 'idade': idade, 'sexo': sexo})

media_idade = sum(p['idade'] for p in pessoas) / n

mulheres_menos_20 = sum(1 for p in pessoas if p['sexo'] == 'F' and p['idade'] < 20)

print(f"\nA média de idade do grupo é {media_idade:.2f} anos.")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menos_20}")