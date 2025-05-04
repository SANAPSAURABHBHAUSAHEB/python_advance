import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = arr1.copy()
arr3 = arr2.view()

print(arr1)
print(arr2)
print(arr3)
print()

# arr1 = arr1*6
# arr2 = arr2*6
arr3 = arr3*6

print()
print(arr2)
print(arr3)
print(arr1)