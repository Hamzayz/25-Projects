from func import Functions

function = Functions()

running = True
while running:
    print("1. Add Expense")
    print("2. Update Expense")
    print("3. Remove Expense")
    print("4. view Expenses")
    print("5. Summary of Expenses")
    print("6. Search Expenses")
    print("7. Filter Expenses by Date")
    print("8. Exit")
    choice = input("Enter you choice: ")

    if choice == "1":
        title = input("Enter the title of the expense: ")
        amount = input("Enter the amount of the expense: ")
        category = input("Enter the category of the expense: ")
        date = input("Enter the date of the expense (YYYY-MM-DD): ")
        description = input("Enter a description for the expense: ")
        function.add(title, amount, category, date, description)

    elif choice == "2":
        expense_id = input("Enter the ID of the expense to update: ")
        title = input("Enter the new title of the expense (leave blank to keep unchanged): ")
        amount = input("Enter the new amount of the expense (leave blank to keep unchanged): ")
        category = input("Enter the new category of the expense (leave blank to keep unchanged): ")
        date = input("Enter the new date of the expense (YYYY-MM-DD, leave blank to keep unchanged): ")
        description = input("Enter a new description for the expense (leave blank to keep unchanged): ")
        function.update_expence(expense_id, title or None, amount or None, category or None, date or None, description or None)

    elif choice == "3":
        expense_id = input("Enter the ID of the expense to remove: ")
        function.remove(expense_id)

    elif choice == "4":
        function.view()

    elif choice == "5":
        function.summary()

    elif choice == "6":
        keyword = input("Enter a keyword to search in expenses: ")
        function.search(keyword)

    elif choice == "7":
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        end_date = input("Enter the end date (YYYY-MM-DD): ")
        function.filter_by_date(start_date, end_date)

    elif choice == "8":
        print("Exiting the program.")
        running = False