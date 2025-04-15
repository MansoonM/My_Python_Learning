
fruits = [str(i) for i in input("Enter fruits using space separate them: ").split()]

newFruits=[]

for x in fruits:
    if "a" in x:
        newFruits.append(x)

print("Fruits: ", fruits)
print("NewFruits having \"a\" ", newFruits)

