# adding item into the tuple

tuple1= (23,54,47,81,36)

# convert a tuple to list
list1= list(tuple1)

# add item to list
list1.append(10)

# convert list to tuple
tuple1=tuple(list1)

print(tuple1)


# ======================================
# removing items from tuple
tuple2=(32, 43, 7, 89, 45, 87)

# tuple to list
list2= list(tuple2)

# remove item at index -1  (last index)
list2.pop()

# list to tuple
tuple2= tuple(list2)

print(tuple2)