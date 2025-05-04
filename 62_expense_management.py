

class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description

    def __str__(self):
        return f"{self.amount} - {self.category}: {self.description}"

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description):
        expense = Expense(amount, category, description)
        self.expenses.append(expense)

    def get_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def get_expenses_by_category(self, category):
        return [expense for expense in self.expenses if expense.category == category]

    def display_expenses(self):
        for expense in self.expenses:
            print(expense)

def main():
    manager = ExpenseManager()

    while True:
        print("\nExpense Manager")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. View Expenses by Category")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            manager.add_expense(amount, category, description)
            print("Expense added.")

        elif choice == '2':
            print("\nAll Expenses:")
            manager.display_expenses()

        elif choice == '3':
            total = manager.get_total_expenses()
            print(f"Total Expenses: {total}")

        elif choice == '4':
            category = input("Enter category: ")
            expenses = manager.get_expenses_by_category(category)
            print(f"\nExpenses in category '{category}':")
            for expense in expenses:
                print(expense)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()