# class and object

# class is a collection of objects. It is a blue print for creating objects.
# class define attributes(variables) and instances(methods) that are created by using objects. 
# myClass.myAttribute



# creating a class name "Dog"
class Dog:
    species="Canine"  # class attribute
    def __init__(self,name,age):
        self.name=name # Instance attribute
        self.age=age  # Instance attribute
        

# Objects can anything. Here, Object is the intances of class,
#  It represents a specific implementation of the class and hold its own data.
# myVariable=myClass(myAttribute1,myAttribute2...)


# creating object to access class
dog1= Dog("john",6)

# printing data
print(dog1.name, dog1.age, dog1.species)  # using object
print(Dog.species) # directly using class

