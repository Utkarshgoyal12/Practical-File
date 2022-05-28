#4.you are given 2 integer arrays A and B.Perform the following operations.
# 1.Add
# 2.Subtract
# 3.Multiply
# 4.Integer Division
# 5.Mod
# 6.Power
import numpy as np
a=[1,2,3,4]
b=np.array([[5,6,7,8]])
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.floor_divide(a,b))
print(np.mod(a,b))
print(np.power(a,b))