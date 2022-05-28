# Q-->write a python function to find the sum of all numbers in a list.
def add(numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum
numbers=input("entre the numbers").split()
numbers=list(map(int,numbers))
a=add(numbers)
print(a)