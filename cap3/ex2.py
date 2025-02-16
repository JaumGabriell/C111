loja1 = {
    'disponivel': ['acer', 'dell', 'hp'],
    'indisponivel': ['lenovo', 'samsung']
}
loja2 = {
    'disponivel': ['acer', 'dell', 'hp', 'lenovo', 'samsung']
}

print("Loja 1 - Disponíveis:", loja1['disponivel'])
print("Loja 1 - Indisponíveis:", loja1['indisponivel'])
print("Loja 2 - Disponíveis:", loja2['disponivel'])

disponiveis_ambas = list(set(loja1['disponivel']).intersection(loja2['disponivel']))
print("\nDisponíveis em ambas as lojas:", disponiveis_ambas)