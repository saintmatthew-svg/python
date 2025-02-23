expenses = []

def print_menu():
    print("""
        Welcome to Semicolon Expense Tracker App
        -—-----------------------------------------
        
        1. Add an expense
        2. View all expenses
        3. Calculate total expenses
        4. Exit
        
        """)

def add_expense():
    date = input("Enter the date: (YYYY-MM-DD): ") 
    description = str(input("Enter the Description: "))
    amount = float(input("Enter the amount: "))
    expenses.append({'date': date, 'description': description, 'amount': amount})
    print("Expense added!\n")   
      
def view_expenses():
    print("Expenses: ")
    for expense in expenses:
        print(f"Date: {expense['date']}, Description: {expense['description']}, Amount: {expense['amount']}")
    if not expenses:
        print("No expenses recorded yet.\n")
            
def calculate_expenses():
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Expenses: {total}\n")
    
    
def main():
    print_menu()
    while True:
        print("")
        choice = int(input("enter your choice (1/2/3/4): "))
        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            calculate_expenses()
        elif choice == 4:
            print(" EXITING THE APP. GOODBYE! ")
            break
        else:
            print("Invalid choice. please try again.")
        print_menu()
main()