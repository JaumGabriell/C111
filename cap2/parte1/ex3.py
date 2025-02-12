s = ''

while s != 'M' and s != 'F':

    s = input('digite o M para homem ou F para mulher: ')

    if s == 'M':
        print('Masculino')
    elif s == 'F':
        print('Feminino')
    else:
        print('Sexo inválido')
    s = input('digite o M para homem ou F para mulher: ')

