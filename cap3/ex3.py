nome = input("Digite o nome do aluno: ")
media = float(input("Digite a média do aluno: "))


aluno = {
    'nome': nome,
    'media': media
}


if media >= 50:
    aluno['situacao'] = 'AP'  
else:
    aluno['situacao'] = 'RP'  

print("\nConteúdo do dicionário do aluno:")
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")