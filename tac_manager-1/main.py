from func import Functions

function = Functions()

running = True

while running:
    print("Welcome to the Task-Manager!")

    print("What would you like to do?")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. View all tasks")
    print("4. Mark task as completed")
    print("5. View task statistics")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        "\n"
        print("Select priority:")
        print("1. High")
        print("2. Medium")
        print("3. Low")
        priority = input("Enter priority (1-3): ")
        if priority == "1" :
            priority = "High"
        elif priority == "2":
            priority = "Medium"
        elif priority == "3":
            priority = "Low"

        end_date = int(input("Enter number of days until due date: "))

        print("Select category: ")
        print("1. Work\n2. Personal\n3. Shopping\n4. Health")
        category = input("Enter category number: ")

        if category == "1":
            category = "Work"
        elif category == "2":
            category = "Personal"
        elif category == "3":
            category = "Shopping"
        elif category == "4":
            category = "Health"

        function.add(title, description, priority, category, end_date)
    
    elif choice == "2":
        task_id = input("Enter the Task ID to remove: ")
        function.remove(task_id)

    elif choice == "3":
        function.view_all()

    elif choice == "4":
        task_id = input("Enter the Task ID to mark as completed: ")
        function.mark_completed(task_id)

    elif choice == "5":
        function.statistics()
    
    elif choice == "6":
        running = False
        print("Exiting Task-Manager. Goodbye!")