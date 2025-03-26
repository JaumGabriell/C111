import pandas as pd

# 1. Criando as Series
seriesAno1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
seriesAno2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

# 2. Calculando a porcentagem total de mercado para cada ano
totalAno1 = seriesAno1.sum()
totalAno2 = seriesAno2.sum()

print(f"Porcentagem total no mercado no Ano 1: {totalAno1:.2f}%")
print(f"Porcentagem total no mercado no Ano 2: {totalAno2:.2f}%")

# 3. Calculando o crescimento/declínio no mercado de cada linguagem
variacao = seriesAno2 - seriesAno1
print("\nCrescimento/Declínio no mercado de cada linguagem:")
print(variacao)

# 4. Mostrando apenas as linguagens que tiveram crescimento
crescimento = variacao[variacao > 0]
print("\nLinguagens que tiveram crescimento:")
print(crescimento)

# 5. Projetando o crescimento/declínio para os próximos 2 anos
projecaoAno3 = seriesAno2 + variacao
projecaoAno4 = projecaoAno3 + variacao

# Encontrando a linguagem mais popular no Ano 4
linguagemMaisPopular = projecaoAno4.nlargest(1)
print("\nLinguagem mais popular no Ano 4 (projeção):")
print(linguagemMaisPopular)