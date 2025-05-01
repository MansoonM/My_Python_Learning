# Cafe raw material management system

fruits = ["Apple", "Orange", "Watermelon", "Banana", "Kiwi", "Strawberry", "Cherry"]
ration_items = ["Coffee", "Tea", "Sugar", "Salt", "Baking Powder", "Soda", "Lemon", "Chilli", "Honey", "Curd", "Milk", "Ice", "Milk Powder"]
cleaning_items = ["Detol", "Hand Sanitizer", "Soap"]
snacks_side_food_items = ["Biscuit", "Cookies", "Chocolate", "Cakes", "Pancakes", "Salad"]

menu = fruits + ration_items + cleaning_items + snacks_side_food_items

print("=================================")
print("Cafe Raw Materials")
print("=================================")
for x in menu:
    print(x) 
print("=================================")

# User inputs
add = input("Add items (comma-separated): ").split(',')
remove = input("Remove items (comma-separated): ").split(',')
update = input("Update item (format: old_item,new_item): ")

# To perform operations on menu items
def addItems(menu, items):
    for item in items:
        item = item.strip()  # Remove any leading/trailing whitespace
        if item not in menu:  # Avoid duplicates
            menu.append(item)

def removeItems(menu, items):
    for item in items:
        item = item.strip()  # Remove any leading/trailing whitespace
        if item in menu:
            menu.remove(item)

def updateItems(menu, update_str):
    if ',' in update_str:
        old_item, new_item = map(str.strip, update_str.split(','))
        if old_item in menu:
            index = menu.index(old_item)
            menu[index] = new_item  # Update the item

# Perform operations
addItems(menu, add)
removeItems(menu, remove)
updateItems(menu, update)

# Print updated menu
print("=================================")
print("Updated Cafe Raw Materials")
print("=================================")
for x in menu:
    print(x)
print("=================================")