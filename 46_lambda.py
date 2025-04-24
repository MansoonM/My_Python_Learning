# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# lambda arguments : expression

# here a is argument

# code 1
num= lambda a: a+ 10
# accessing lambda values
print(num(9))


# code 2
x = lambda a, b : a * b
print(x(5, 6))

# code 3
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))



# code 4
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))