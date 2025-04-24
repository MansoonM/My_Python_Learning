# Build a mini store to add and remove items inside the store


add_fruit=input("Enter the fruit name to add: ")
def addItems(add_fruit):
      store=["cherry","papaya","banana","apple","kiwi"]
      if add_fruit not in store:
            store.append(add_fruit)
      else:
        return "Already Existing in store."
      return store

result_after_adding=addItems(add_fruit)
print(result_after_adding)     
      
   



remove_fruit=input("Enter the fruit name to remove: ")

def removeItems(remove_fruit):
    store=["cherry","papaya","banana","apple","kiwi"]
    if remove_fruit in store:
        store.remove(remove_fruit)
    else:
        return "Item does not exist in store"
    return store   

result_after_removing= removeItems(remove_fruit)
print(result_after_removing)
