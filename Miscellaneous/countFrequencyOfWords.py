#Q-->wap to count the frequency of words in a file.
f=open("sample.txt",'r')
a=f.read().split()
b=set(a)
b=list(b)
for i in b:
    print(i,'=',a.count(i))
f.close()
