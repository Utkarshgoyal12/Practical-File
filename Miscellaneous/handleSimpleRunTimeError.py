#Q-->python program to handle simple run time error.
try:
    a=[1,2,3,4]
    n=int(input())
    print(a[n])
except:
    print("An error occured")
else:
    print("number has been print successfully")