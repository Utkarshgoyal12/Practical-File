#Q-->wap to append text to a file and display the text.
f=open('sample.txt','a')
a=input("entre the text")
f.write(a)
f.close()
f=open("sample.txt",'r')
print(f.read())
f.close()
