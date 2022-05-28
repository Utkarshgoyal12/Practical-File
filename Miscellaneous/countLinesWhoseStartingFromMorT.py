#Q--Write a program in python to count those lines from the file “div.txt” which are starting from ‘T’ or ‘M’.
f=open("div.txt", "r")
d=f.readlines()
c=0
for i in d:
     if i[0] == 'M' or i[0] == 'T':
        c=c+1
print("Total lines are :", c)
