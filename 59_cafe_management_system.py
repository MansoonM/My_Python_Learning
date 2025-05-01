# cafe management system

# our order items
menu={
    "cold coffee": 120,
    "hot coffee": 120,
     "chocolate coffee": 150,
     "tea":70,
     "masala tea": 110,
     "green tea": 120,
    "cookies": 100,
    "chicken pizza": 150,
    "panner pizza": 100,
    "chicken burger": 100,
    "panner burger": 80,
    "oreo shake": 150,
    "chicken popcorn":120
}
print("==================================")
print("Menu Of Our Cafe Shop: ")
print("==================================")



for item, price in menu.items():
    print(f"{item}: {price}")
print("==================================")

# Taking the order
order = input("Enter your order (comma-separated items): ").lower().split(',')

# Initialize total amount
total_amount = 0
ordered_items = {}

# Calculate total and prepare ordered items
for item in order:
    item = item.strip()  # Remove any leading/trailing whitespace
    if item in menu:
        ordered_items[item] = menu[item]
        total_amount += menu[item]
    else:
        print(f"Sorry, we don't have {item} in the menu.")

# Generate the bill
print("\n==================================")
print("Your Order Bill:")
print("==================================")
for item, price in ordered_items.items():
    print(f"{item}: {price}")
print("==================================")
print(f"Total Amount: {total_amount}")
print("==================================")
