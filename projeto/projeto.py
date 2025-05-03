import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('screen_time.csv', delimiter=',')

def ScreenTime5anos():
    # Filtrar crianças de 5 anos com mais de 1 hora de tempo de tela
    criancas_5_anos = df[(df['Age'] == 5) & (df['Average Screen Time (hours)'] >= 1)]

    # Contar o número de crianças
    numero_criancas = 0
    numero_criancas = criancas_5_anos['Sample Size'].sum() + numero_criancas

    # Imprimir o resultado
    print(f"Número de crianças de 5 anos com mais de 1 hora de tempo de tela: {numero_criancas}")

    # Criando gráfico de pizza do tempo de tela entre as crianças que estão acima da média de 1 hora e as que estão abaixo entre as crianças de 5 anos

    # Filtrar crianças de 5 anos com 1 hora ou menos de tempo de tela
    criancas_5_anos_abaixo = df[(df['Age'] == 5) & (df['Average Screen Time (hours)'] < 1)]

    # Contar o número de crianças em cada grupo
    numero_acima = criancas_5_anos['Sample Size'].sum()
    numero_abaixo = criancas_5_anos_abaixo['Sample Size'].sum()

    #    Dados para o gráfico de pizza
    labels = ['1 hora ou mais', 'Menos de 1 hora']
    sizes = [numero_acima, numero_abaixo]
    colors = ['#ff9999', '#66b3ff']
    explode = (0.1, 0)  # Destacar o primeiro pedaço

    # Criar o gráfico de pizza
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', startangle=90)
    plt.title('Proporção de crianças de 5 anos por tempo de tela')
    plt.axis('equal')  # Garantir que o gráfico seja um círculo
    plt.show()


# Quantidade de crianças de 5 anos com mais de 1 hora de tempo de tela e gráfico de pizza
#ScreenTime5anos()


def ScreenTime6e11anos():
    # Filtrar crianças de 5 anos com mais de 1 hora de tempo de tela
    criancas_entre_6_e_11_anos = df[(df['Age'] >= 5) & (df['Age'] <= 11) & (df['Average Screen Time (hours)'] >= 2)]

    # Contar o número de crianças
    numero_criancas = 0
    numero_criancas = criancas_entre_6_e_11_anos['Sample Size'].sum() + numero_criancas

    # Imprimir o resultado
    print(f"Número de crianças de 5 anos com mais de 1 hora de tempo de tela: {numero_criancas}")

    # Criando gráfico de pizza do tempo de tela entre as crianças que estão acima da média de 1 hora e as que estão abaixo entre as crianças de 5 anos

    # Filtrar crianças de 5 anos com 1 hora ou menos de tempo de tela
    criancas_entre_6_e_11_anos_abaixo= df[(df['Age'] >= 5) & (df['Age'] <= 11) & (df['Average Screen Time (hours)'] < 2)]

    # Contar o número de crianças em cada grupo
    numero_acima = criancas_entre_6_e_11_anos['Sample Size'].sum()
    numero_abaixo = criancas_entre_6_e_11_anos_abaixo['Sample Size'].sum()

    #    Dados para o gráfico de pizza
    labels = ['2 horas ou mais', 'Menos de 2 horas']
    sizes = [numero_acima, numero_abaixo]
    colors = ['#ff9999', '#66b3ff']
    explode = (0.1, 0)  # Destacar o primeiro pedaço

    # Criar o gráfico de pizza
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', startangle=90)
    plt.title('Proporção de crianças entre 6 e 11 anos por tempo de tela')
    plt.axis('equal')  # Garantir que o gráfico seja um círculo
    plt.show()


# Quantidade de crianças de 6 a 11 anos com mais de 2 horas de tempo de tela e gráfico de pizza
ScreenTime6e11anos()

def ScreenTimeMaior11anos():
    # Filtrar crianças de 5 anos com mais de 1 hora de tempo de tela
    criancas_maior_11_anos = df[(df['Age'] > 11) & (df['Average Screen Time (hours)'] >= 3)]

    # Contar o número de crianças
    numero_criancas = 0
    numero_criancas = criancas_maior_11_anos['Sample Size'].sum() + numero_criancas

    # Imprimir o resultado
    print(f"Número de crianças de 5 anos com mais de 1 hora de tempo de tela: {numero_criancas}")

    # Criando gráfico de pizza do tempo de tela entre as crianças que estão acima da média de 1 hora e as que estão abaixo entre as crianças de 5 anos

    # Filtrar crianças de 5 anos com 1 hora ou menos de tempo de tela
    criancas_maior_11_anos_abaixo= df[(df['Age'] > 11) & (df['Average Screen Time (hours)'] < 3)]

    # Contar o número de crianças em cada grupo
    numero_acima = criancas_maior_11_anos['Sample Size'].sum()
    numero_abaixo = criancas_maior_11_anos_abaixo['Sample Size'].sum()

    #    Dados para o gráfico de pizza
    labels = ['3 horas ou mais', 'Menos de 3 horas']
    sizes = [numero_acima, numero_abaixo]
    colors = ['#ff9999', '#66b3ff']
    explode = (0.1, 0)  # Destacar o primeiro pedaço

    # Criar o gráfico de pizza
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%1.1f%%', startangle=90)
    plt.title('Proporção de crianças maiores que 11 anos por tempo de tela')
    plt.axis('equal')  # Garantir que o gráfico seja um círculo
    plt.show()
