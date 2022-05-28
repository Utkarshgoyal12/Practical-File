#Q--Write a program in python to display only unique words from the file “story.txt”.
f = open("story.txt", "r")
d = f.read()
d = d.split()
str = " "
m = []
for i in d:
  if i not in str:
       str=str+i
       print(i, end=" ")
f.close()