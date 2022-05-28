# Q--> Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique(a):
    x=[]
    for i in a:
        if i not in x:
            x.append(i)
    return x
a=(input("enter the numbers")).split()
a=list(map(int,a))
c=unique(a)
print(c)