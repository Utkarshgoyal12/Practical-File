#7.Write a program in python to find the occurances of elements or pair of elements in an array.
import numpy as np
a=np.array([[1, 2, 3],
            [2, 3, 4],
            [2, 3, 5]])
            
out=repr(a).count('2, 3')

print(out)
