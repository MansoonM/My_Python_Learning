# list are like arrays in python
# =================================================
# Accessing elements in List
# =================================================
# number list
list=[1,2,34,4,8] # this is a list
print(list[0])  # to print one element

# to print all
for i in list:
    print(i, "increment of i is ", i+1)

# alphabet list
list_alpha=["A","B","C"]

# last element
print(list_alpha[-1])

# print all element
for i in list_alpha:
    print(i)

# =================================================
# Adding a new element into the List
# =================================================

# adding an integer/number
list.append(45)
print(list[-1])

for i in list:
    print(i)

# adding an alphabet 
list_alpha.append("D")
print(list_alpha[-1])

for i in list_alpha:
    print(i)

# =================================================
# Change an element in the List
# =================================================

new_list=["mango","apple","orange","banana"]

for i in new_list:
    print(i)

# change banana -> guava
new_list[-1]="guava"
for i in new_list:
    print(i)