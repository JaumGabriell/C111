# Tuplas são coleções de dados ordenadas e imutáveis

nomes = ('goku', 'vegeta', 'gohan', 'piccolo')
print(nomes)

# slice de dados

print(nomes[0]) #goku
print(nomes[:2]) #goku e vegeta
print(nomes[2:]) #gohan e piccolo
print(nomes[1:3]) #vegeta e gohan
print(nomes[-1]) #piccolo

#listas são coleções de dados ordenadas e mutáveis

nomes2 = ['goku', 'vegeta', 'gohan', 'piccolo']

#insert

nomes2.append('kuririn') #adiciona um elemento no final da lista
nomes2.insert(1, 'yamcha') #adiciona um elemento na posição 1
print(nomes2)

#update

nomes2[1] = 'goten' #altera o elemento na posição 1

# delete

del nomes2[1] #deleta o elemento na posição 1
nomes2.remove('gohan') #remove o elemento gohan

print(nomes2)

if 'goku' in nomes2:
    print('goku está na lista') #verifica se goku está na lista

# conjuntos (sets) são coleções de dados não ordenadas e sem elementos duplicados

nomes3 = {'goku', 'vegeta', 'gohan', 'piccolo', 'goku'}

print(nomes3) #goku não será impresso duas vezes

#adicionando elementos

nomes3.add('kuririn')

#deletando elementos

nomes3.remove('goku')

#dicinários são coleções de dados não ordenadas, mutáveis e indexadas

pessoa = {'nome': 'goku', 'raça': 'saiyajin', 'idade': 30}

print(pessoa)
# acessando elementos
print(pessoa['nome'])
#adicionando elementos
pessoa['sexo'] = 'masculino'
#update
pessoa['idade'] = 35
#delete
del pessoa['sexo']