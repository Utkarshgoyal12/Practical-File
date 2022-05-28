#5.Write a program in python to print the transpose and flatten of a given integer array matrix.
import numpy as np
lst=[]
r=int(input('enter no of rows'))
c=int(input('enter no of col'))
for i in range(r):
    for j in range(c):
        ele=int(input('enter element'))
        lst.append(ele)
a=np.array(lst).reshape(r,c)
print(np.transpose(a))
print(np.ravel(a))