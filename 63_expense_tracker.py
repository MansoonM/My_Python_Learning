# Initialize an empty list to store expenses
expenses = []

def add_expense(amount, category, description):
    """Add an expense to the expenses list."""
    expense = {
        'amount': amount,
        'category': category,
        'description': description
    }
    expenses.append(expense)
    print("Expense added.")

def get_total_expenses():
    """Calculate and return the total expenses."""
    return sum(expense['amount'] for expense in expenses)

def get_expenses_by_category(category):
    """Return a list of expenses filtered by category."""
    return [expense for expense in expenses if expense['category'] == category]

def display_expenses():
    """Display all expenses."""
    if not expenses:
        print("No expenses recorded.")
        return
    for expense in expenses:
        print(f"{expense['amount']} - {expense['category']}: {expense['description']}")

def main():
    while True:
        print("-----------------------------------")
        print("\nExpense Manager")
        print("-----------------------------------")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. View Expenses by Category")
        print("5. Exit")
        print("-----------------------------------")
        choice = input("Choose an option: ")
        print("-----------------------------------")

        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            add_expense(amount, category, description)

        elif choice == '2':
            print("\nAll Expenses:")
            display_expenses()

        elif choice == '3':
            total = get_total_expenses()
            print(f"Total Expenses: {total}")

        elif choice == '4':
            category = input("Enter category: ")
            expenses_in_category = get_expenses_by_category(category)
            print(f"\nExpenses in category '{category}':")
            for expense in expenses_in_category:
                print(f"{expense['amount']} - {expense['description']}")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()