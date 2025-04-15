    # remove() -> remove particular item
    #  pop() -> remove specified index item
    # , del() 
    # clear() -> empty the list

# use remove()
list1=["Mango","Guava","Watermelon"]
list1.remove("Guava")
print(list1)


list2=["Banana","Orange","Grapes","Watermelon","Mango"] 
list2.pop()  #last index
list2.pop(1) #specified index
print(list2)

list3=["car","Truck","Bike","Scooty"]
del list3[1]
print(list3) 

# del list3 
# print(list3)

# clear()