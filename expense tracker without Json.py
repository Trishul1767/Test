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

def sort_expenses_by_date():
    if not os.path.exists("expenses.txt"):
        print("No expenses recorded yet.")
        return

    # Ask the user for the date in YYYY-MM-DD format
    search_date = input("Enter the date to filter (YYYY-MM-DD): ")
    found = False
    
    print(f"\n--- Expenses for {search_date} ---")
    with open("expenses.txt", "r") as f:
        for line in f:
            # line.split("|") creates a list: [category, amount, date]
            parts = line.split("|")
            if len(parts) == 3:
                # parts[2] is the date string " 2023-10-27 10:30:00"
                # .strip() removes spaces, and we check if it starts with the search_date
                file_date = parts[2].strip()
                if file_date.startswith(search_date):
                    print(line.strip())
                    found = True
    
    if not found:
        print("No expenses found for this date.")
        


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
    print('4. Sort Expenses by Date')
    print('5. Delete Expenses')
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        view_total_expenses()
    elif choice == "4":
        sort_expenses_by_date()
    elif choice == "5":
        delete_expenses()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")
