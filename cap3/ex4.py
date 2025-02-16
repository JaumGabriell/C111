pessoas = []

for i in range(3):
    nome = input(f"Digite o nome da pessoa {i+1}: ")
    peso = float(input(f"Digite o peso da pessoa {i+1} (em kg): "))
    pessoas.append({'nome': nome, 'peso': peso})

mais_pesada = max(pessoas, key=lambda p: p['peso'])
mais_leve = min(pessoas, key=lambda p: p['peso'])

print(f"\nA pessoa mais pesada é {mais_pesada['nome']} com {mais_pesada['peso']} kg.")
print(f"A pessoa mais leve é {mais_leve['nome']} com {mais_leve['peso']} kg.")