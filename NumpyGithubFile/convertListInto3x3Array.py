#2.Write a program in python to convert the given list into 3*3 array.
import numpy as np
a=list(map(int,input().split()))
print(np.array(a).reshape(3,3))