# Q-->wap in python to find the multiply of all the items in a dictionary.
a={}
size=int(input("enter the size"))
for i in range(0,size):
    x=int(input('enter the key'))
    y=int(input("enter the value"))
    a.update({x:y})
mul=1
for i in (a.values()):
    mul=mul*i
print(mul)