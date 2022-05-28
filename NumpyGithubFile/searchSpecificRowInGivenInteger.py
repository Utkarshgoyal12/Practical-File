#6.Write a program in python to search a specified row in a given integer matrix array.
import numpy as np
a=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
print(a)

print([1,2,3] in a.tolist())

print([4,5,6] in a.tolist())