# expense tracker without Json
import datetime

expenses = []

def add_expense():
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    expenses.append({"description": description, "amount": amount, "date": date})

def view_expenses():
    for expense in expenses:
        print(f"Description: {expense['description']}, Amount: {expense['amount']}, Date: {expense['date']}")

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")