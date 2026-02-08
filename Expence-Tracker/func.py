import random
import pandas as pd
import os

class Functions():
    def __init__(self,):
        self.expense_id = None
        self.file_path = os.path.join(os.path.dirname(__file__), "expenses.csv")

    def generate_id(self):
        self.expense_id = "".join(str(random.randint(1, 9))for _ in range(4))
        return self.expense_id
    
    def add(self, title, amount, category, date, description):
        data = {
            "ID" : int(self.generate_id()),
            "Title" : title,
            "Amount" : int(amount),
            "Category" : category,
            "Date" : date,
            "Description" : description
        }
        try:
            df = pd.read_csv(self.file_path)
            df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)

        except FileNotFoundError:
            df = pd.DataFrame([data])
        df.to_csv(self.file_path, index=False)

        print(f"Expense added with ID: {data['ID']}")

    def remove(self, expense_id):
        try:
            df = pd.read_csv(self.file_path)
            df = df[df["ID"] != int(expense_id)]
            df.to_csv(self.file_path, index=False)
            print(f"Expense with ID {expense_id} removed.")
        except FileNotFoundError:
            print("No expenses to remove.")

    def update_expence(self, expense_id, title=None, amount=None, category=None, date=None, description=None):
        try:
            df = pd.read_csv(self.file_path)
            if title is not None:
                df.loc[df["ID"] == int(expense_id), "Title"] = title
            if amount is not None:
                df.loc[df["ID"] == int(expense_id), "Amount"] = int(amount)
            if category is not None:
                df.loc[df["ID"] == int(expense_id), "Category"] = category
            if date is not None:
                df.loc[df["ID"] == int(expense_id), "Date"] = date
            if description is not None:
                df.loc[df["ID"] == int(expense_id), "Description"] = description
            df.to_csv(self.file_path, index=False)
            print(f"Expense with ID {expense_id} updated.")
        except FileNotFoundError:
            print("No expenses to update.")

    def view(self):
        try:
            df = pd.read_csv(self.file_path)
            print(df)
        except FileNotFoundError:
            print("No expenses to show.")
    
    def summary(self):
        try:
            df = pd.read_csv(self.file_path)
            summary = df.groupby("Category")["Amount"].sum()
            print(summary)
        except FileNotFoundError:
            print("No expenses to summarize.")

    def search(self, keyword):
        try:
            df = pd.read_csv(self.file_path)
            results = df[df["Title"].str.contains(keyword, case=False, na=False) | df["Description"].str.contains(keyword, case=False, na=False)]
            if not results.empty:
                print(results)
            else:
                print("No matching expenses found.")
        except FileNotFoundError:
            print("No expenses to search.")

    def filter_by_date(self, start_date, end_date):
        try:
            df = pd.read_csv(self.file_path)
            filtered = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]
            if not filtered.empty:
                print(filtered)
            else:
                print("No expenses found in the given date range.")
        except FileNotFoundError:
            print("No expenses to filter.")