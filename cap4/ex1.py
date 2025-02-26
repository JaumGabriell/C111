import numpy as np

arr = np.ones(8)

arr2 = np.random.randint(0,9, size=(8))

arr3 = arr + arr2

print(arr3)

arr4 = arr3.sum()

print(arr4)

if arr4 >= 40:
    mtz = arr3.reshape(4,2)
    print(mtz)
else:
    mtz = arr3.reshape(2,4)
    print(mtz)