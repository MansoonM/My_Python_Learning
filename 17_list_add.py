# adding items in various method in python
# 3 ways to add items into the list
# 1. append() -> element add at last of list
# 2. insert() -> element add at spefied position of list(1,"apple")
# 3. extend() -> adding to list together 

list1=["Mango","Guava","Watermelon"]

list2=["Banana","Orange","Grapes"]

# add new item "Kiwi" to list1 at last index
list1.append("Kiwi")
for x in list1:
    print(x)

# add new item "Apple" to list2 at index[2]
list2.insert(2,"Apple")
for y in list2:
    print(y)

# combine two list
list1.extend(list2)
print(list1)