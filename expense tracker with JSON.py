#expense tracker
import json
import os
class ExpenseTracker:
    def __init__(self, filename='expenses.json'):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_expenses(self):
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, category, description):
        expense = {
            'amount': amount,
            'category': category,
            'description': description
        }
        self.expenses.append(expense)
        self.save_expenses()

    def view_expenses(self):
        for expense in self.expenses:
            print(f"Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")

    def total_expenses(self):
        return sum(expense['amount'] for expense in self.expenses)
if __name__ == "__main__":
    tracker = ExpenseTracker()
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            tracker.add_expense(amount, category, description)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            print(f"Total Expenses: {tracker.total_expenses()}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")