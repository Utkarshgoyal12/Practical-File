# Q-->wap in python to map two lists into  a dictionary.
key=input("enter the keys").split()
key=list(map(int,key))
value=input("enter the values").split()
value=list(map(int,value))
dict=dict(zip(key,value))
print(dict)