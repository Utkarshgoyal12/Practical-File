# Q-->write a python function to reverse the order of words in a string.
def order_reverse(str):
    str.reverse()
    return " ".join(str)
str=input("entre the string").split()
c=order_reverse(str)
print(c)