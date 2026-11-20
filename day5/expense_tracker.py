print("========== EXPENSE TRACKER ==========")
print(
    "1. Add an expense\n2. View all expenses\n3. View total spending\n4. View spending by category\n5. Exit" 
)
all_expenses = []
while True:
    choice = input("Choose an option: ")
    if choice == "1":
        while True:
            name = input("Enter expense name: ")
            while name == "":
                print("Name can not be empty.")
                name = input("Enter expense name: ")
            else:
                while True:
                    try:
                        amount = int(input("Enter expense amount: "))
                        if amount > 0:
                            break
                    except ValueError:
                        print("Amount has to be an integer")
                category = input("Enter expense category: ")
                while category == "":
                    print("Category can not be empty.")
                    category = input("Enter expense category: ")
                entry = {
                    "name": name,
                    "amount": amount,
                    "category": category,
                }
                all_expenses.append(entry)
                break
    elif choice == "2":
        if not all_expenses:
            print("No expenses added yet.")
        else:
            for index , expense in enumerate(all_expenses, start=1):
                        print(f"Expense {index}")
                        for key, value in expense.items():
                            print(f"{key}: {value}")
    elif choice == "3":
        if not all_expenses:
            print("No expenses added yet.")
        else:
             total = 0
             for count, d in enumerate(all_expenses):
                  total = total + d.get('amount', 0)
        print("========== TOTAL SPENDINGS ==========")
        print(f"Total Expenses: {count + 1}")
        print("Total amount spent: ₹",total)

    elif choice == "4":
        if not all_expenses:
            print("No expenses added yet.")
        else:
            category_wise_expenses = {}
            for expense in all_expenses:
                category = expense["category"]
                amount = expense["amount"]
                if category in category_wise_expenses:
                    category_wise_expenses[category] = category_wise_expenses[category] + amount
                else:
                    category_wise_expenses[category] = amount
            print("========== CATEGORY SUMMARY ==========")

            for category, total in category_wise_expenses.items():
                print(f"{category}: ₹{total}")

    elif choice == "5":
        print("Thanks for using the expense tracker.")
        break
    else:
        print("Select a valid option from the menu.")