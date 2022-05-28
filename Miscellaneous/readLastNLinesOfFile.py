#Q-->wap to read the last n lines of a file.
n=int(input("entre the no. of lines"))
with open("sample.txt")as f:
    print(list(f)[-n:])