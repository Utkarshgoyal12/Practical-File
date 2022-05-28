#Q-->wap to find the longest word in a file.
f=open('sample.txt','r')
a=f.read().split()
print(max(a,key=len))
