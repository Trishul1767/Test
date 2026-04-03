# expense tracker without Json but with file handling
import datetime
import os

def add_expense():
    try:
        amount = float(input("Enter expense amount: "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return
    category = input("Enter expense category: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("expenses.txt", "a") as f:
        f.write(f"{category} | {amount} | {date}\n")

def view_expenses():
    if not os.path.exists("expenses.txt"):
        print("No expenses recorded yet.")
        return
    else:
        with open("expenses.txt", "r") as f:
            for line in f:
                print(line.strip())
def view_total_expenses():
    total = 0
    if not os.path.exists("expenses.txt"):
        print("No expenses recorded yet.")
        return
    else:
        with open("expenses.txt", "r") as f:
            for line in f:
                try:
                    amount = float(line.split("|")[1].strip())
                    total += amount
                except (IndexError, ValueError):
                    continue
    print(f"Total Expenses: {total}")

def delete_expenses():
    if os.path.exists("expenses.txt"):
        os.remove("expenses.txt")
        print("All expenses deleted successfully.")
    else:
        print("No expenses to delete.")

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expenses")
    print('4. Delete Expenses')
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        view_total_expenses()
    elif choice == "4":
        delete_expenses()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")