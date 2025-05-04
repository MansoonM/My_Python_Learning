
'''  Explaination    '''
''' 
Inheritance is an oops concept that involves Parent-Child Relationship.
Parent Class is also called Base Class.
Child Class is also called Derived Class.
It allows child class to acquire properties of it's parent class.

There are 5 types of Inheritance:
1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance
4. Hierarchial Inheritance
5. Hybrid Inheritance

'''


'''  ---Working with Inheritance---   '''


# Parent Class
class Dog:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Dog's Name: {self.name}")


# single Inheritance
class Labrador(Dog):  
    def sound(self):
        print("Labrador woofs")

# Multilevel Inheritance
class GuideDog(Labrador):  # Multilevel Inheritance
    def guide(self):
        print(f"{self.name}Guides the way!")



# Multiple Inheritance
class Friendly:
    def greet(self):
        print("Friendly!")

class GoldenRetriever(Dog, Friendly):  # Multiple Inheritance
    def sound(self):
        print("Golden Retriever Barks")

# Example Usage
lab = Labrador("Buddy")
lab.display_name()
lab.sound()

guide_dog = GuideDog("Max")
guide_dog.display_name()
guide_dog.guide()

retriever = GoldenRetriever("Charlie") 
retriever.display_name()
retriever.greet()
retriever.sound()