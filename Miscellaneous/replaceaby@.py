#Q--Write a program in python to replace all the ‘a’ by ‘@’ in a file “data.txt”
f = open("data.txt", "r")
d = f.read()
d = d.replace('a', '@')
f.close()
f=open("data.txt", "w")
f.write(d)
f.close()
