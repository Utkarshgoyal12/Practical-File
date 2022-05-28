#Q--Write a program in python to remove all duplicate lines from the file “story.txt”.
f = open("story.txt", "r")
d = f.readlines()
m = [ ]
for i in d:
     if i not in m:
        m.append(i)
print(m)
f.close()
f = open("story.txt", "w")
for i in m:
     f.write(i)   
f.close()