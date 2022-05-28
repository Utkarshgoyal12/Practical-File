#3.Write a program in python to print an array of size N*M with its main diagonalelements as 1 and 0 everywhere else.
import numpy as np
a=list(map(int,(input('enter order of array').split())))
m=a[0]
n=a[1]
if n==m:
    print(np.identity(n))