#1.Write a program in python to print a reversed numpy array with the element type float.
import numpy as np
a=list(map(int,input('enter your numbers').split()))
a.reverse()
print(np.array(a,dtype=float))