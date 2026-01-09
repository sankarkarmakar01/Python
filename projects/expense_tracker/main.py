# Expense Tracker Project
expense_list = [] # list of all expenses in the form of dictionary

print("Welcome to Expense Tracker 💸")

while True:
    print("======= MENU =======")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. View Total Expense")
    print("4. Exit")

    choice = int(input("Please enter your choice: "))

    # Add Expenses
    if choice == 1:
        date  = input("Enter the date(dd-mm-yyyy): ")
        category = input("Enter category: ")
        description = input("Enter short description: ")
        amount = float(input("Enter amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expense_list.append(expense)
        print("\nExpenses added successfully")

    # View All Expense
    elif choice == 2:
        if len(expense_list) == 0:
            print("No expenses added")
        else:
           print("======= All Expenses =======")
           count = 1
           for each_expense in expense_list:
               print(f"""
               Expense {count} -> 
                        date: {each_expense["date"]}
                        category: {each_expense["category"]}
                        description: {each_expense["description"]}
                        amount: {each_expense["amount"]} """)
               count = count + 1
           print("======= End =======\n")

    # View Total Expense
    elif choice == 3:
        total = 0
        for each_expense in expense_list:
            total += each_expense["amount"]
        print("\nTotal Expenses: ", total)

    # Exit
    elif choice == 4:
        print("Thank You...")
        break

    else:
        print("Invalid choice! Please enter a valid choice.")
