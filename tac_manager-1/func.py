import json
import random
from datetime import datetime, timedelta
from prettytable import PrettyTable

table = PrettyTable()

class Functions:
    def __init__(self):
        self.task_id = None

    def generate_id(self):
        self.task_id = "".join(str(random.randint(1, 9))for _ in range(4))
        return self.task_id

    def add(self, title, description, priority, category, end_date):
        now = datetime.now()
        now_str = now.strftime("%Y-%m-%d")
        due_date = (now + timedelta(days=end_date)).strftime("%Y-%m-%d") if end_date else "None"
        
        task = {
            "ID": self.generate_id(),            
            "Title":title ,
            "Description":description ,
            "Priority":priority ,
            "Category":category,
            "Created_At":now_str if end_date else "None",
            "Due_date" : due_date,
            "Status": "Pending"
        }
        try:
            with open("tac_list.json", "r") as file:
                data = json.load(file)
                # If the stored data is a dict (single task) convert it to a list
                if not isinstance(data, list):
                    data = [data]
                data.append(task)
            # write the updated list back to the file
            with open("tac_list.json", "w") as file:
                json.dump(data, file, indent=4)

        except FileNotFoundError:
            # File doesn't exist yet — create a list with the first task
            data = [task]
            with open("tac_list.json", "w") as file:
                json.dump(data, file, indent=4)
        print(f"Task added with ID: {task['ID']}")
            
    def remove(self, task_id):
        try:
            with open("tac_list.json", "r") as file:
                data = json.load(file)
                data = [task for task in data if task["ID"] != task_id]

            with open("tac_list.json", "w") as file:
                json.dump(data, file, indent=4)
            print("Task removed successfully.")

        except FileNotFoundError:
            print("File not found.")

    def view_all(self):
        try:
            with open("tac_list.json", "r") as file:
                data = json.load(file)
                # Create a fresh table for each view
                view_table = PrettyTable()
                view_table.field_names = ["ID", "Title", "Priority", "Due Date", "Status"]
                
                if isinstance(data, list):
                    for value in data:
                        row = [
                            value.get("ID"),
                            value.get("Title"),
                            value.get("Priority"),
                            value.get("Due_date"),
                            value.get("Status")
                        ]
                        view_table.add_row(row)
                else:
                    # Handle single dict case
                    row = [
                        data.get("ID"),
                        data.get("Title"),
                        data.get("Priority"),
                        data.get("Due_date"),
                        data.get("Status")
                    ]
                    view_table.add_row(row)
                
                print("\n" + "="*60)
                print("ALL TASKS")
                print("="*60)
                print(view_table)
                print("="*60 + "\n")
        except FileNotFoundError:
            print("No tasks found.")
        
    def mark_completed(self, task_id):
        try:
            with open("tac_list.json", "r") as file:
                data = json.load(file)
                for task in data:
                    if task["ID"] == task_id:
                        task["Status"] = "Completed"
                        with open("tac_list.json", "w") as file:
                            json.dump(data, file, indent=4)
                            print("Task marked as completed.")
        except FileNotFoundError:
            print("Invalid Task ID.")

    def statistics(self):
        try:
            with open("tac_list.json", "r") as file:
                data = json.load(file)
                total_tasks = len(data)
                completed_tasks = sum(1 for task in data if task["Status"] == "Completed")
                pending_tasks = total_tasks - completed_tasks
                print("\n" + "="*60)
                print("TASK STATISTICS")
                print("="*60)
                print(f"Total Tasks: {total_tasks}")
                print(f"Completed Tasks: {completed_tasks}")
                print(f"Pending Tasks: {pending_tasks}")
                print("="*60 + "\n")
        except FileNotFoundError:
            print("No tasks available yet.")