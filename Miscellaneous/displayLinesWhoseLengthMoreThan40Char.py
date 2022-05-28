#Q--Write a program in python to read file “data.txt” and display only those lines whose length is more than 40 characters.
f=open("data.txt")
d=f.readlines()
for i in d:
   if len(i)>40:
       print(i)