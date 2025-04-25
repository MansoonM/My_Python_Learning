#  example 1

class person:
    def __init__(self,f_name,l_name):
        self.f_name= f_name
        self.l_name= l_name

# Name is the object calling person class
Name= person("Mansoon", "Mohanty")

print(Name.f_name)
print(Name.l_name)
print(Name.f_name , Name.l_name)


# example 2


class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()