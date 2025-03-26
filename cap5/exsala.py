import pandas as pd
import numpy as np

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]

s1 = pd.Series(index=labels, data=my_data)

print(s1)

#criando com dicionario
s2 = pd.Series({'a': 10, 'c':50, 'd': 80})

#soma de series
print(s1 + s2)

print(s1.add(s2, fill_value=0))

print(s1[['a', 'c']])

print(s1 > s1.mean())
print(s1[s1 > s1.mean()])

np.random.seed(10)

df = pd.DataFrame(index = ['A', 'B', 'C', 'D', 'E'],
                  columns = ['W', 'X', 'Y', 'Z'],
                  data = np.random.randint(1, 50, [5,4]))

print(df)


print(df[['W', 'Z']])

print(df['X']['B'])

print(df.loc[['A', 'B'], ['W','X','Y', 'Z']])