# build a calculator for add,sub,mul,div
def add(a,b):
    c=a+b
    return c

def sub(a,b):
    c=a-b
    return c

def mul(a,b):
    c=a*b
    return c

def div(a,b):
    c=a/b
    return c

first= int(input("Enter a number: "))
second= int(input("Enter a number: "))

print("String Code: add, sub, mul, div")
operation= input("Enter the string code for the Operation: ")

if operation=="add":
    result= add(first,second)
    print(result)
if operation=="sub":
    result= sub(first,second)
    print(result)
if operation=="mul":
    result= mul(first,second)
    print(result)
if operation=="div":
    result= div(first,second)
    print(result)
