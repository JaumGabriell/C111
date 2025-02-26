import numpy as np

arr1 = np.arange(0,51, 2)
arr2 = np.arange(100, 50, -2)

arr3 = np.concatenate((arr1, arr2))

print(np.sort(arr3))