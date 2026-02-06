import requests
import json
from prettytable import PrettyTable
from datetime import datetime

class GithubAPI:
    def __init__(self, username=None, view_user=None):
        self.username = username
        self.view_user = view_user

    def APT(self):
        url = f"https://api.github.com/users/{self.username}/events/public"
        try:
            response = requests.get(url, timeout=10)  # optional timeout
            response.raise_for_status()  # raises HTTPError for 4xx or 5xx
            data = response.json()
            with open("github_events.json", "w") as file:
                json.dump(data, file, indent=4)
                print(f"GitHub events for user '{self.username}' have been saved to 'github_events.json'.")

        except requests.exceptions.RequestException:
            print("Network error or request failed.")
        except json.decoder.JSONDecodeError:
            print("Response is not valid JSON.")
    def view_events(self):
        try:
            with open("github_events.json", "r") as file:
                data = json.load(file)
            if self.view_user:
                print(f"GitHub events for user '{self.view_user}':")
            table = PrettyTable()
            table.field_names = ["Event Type", "Repository", "Created At"]
            for event in data:
                created_date = datetime.fromisoformat(event["created_at"].replace('Z', '+00:00')).strftime('%Y-%m-%d')
                table.add_row([event["type"], event["repo"]["name"], created_date])
            print(table)
        except FileNotFoundError:
            print("No saved GitHub events found.")
        except json.decoder.JSONDecodeError:
            print("Error reading saved GitHub events file.")

print("Welcome to github events viewer!")
running = True

while running:
    print("(1) Fetch and save GitHub events" )
    print("(2) View saved GitHub events")
    print("(3) Exit")
    choice = input("What would you like to do?")

    if choice == "1":
        user = input("Enter your GitHub username: ")
        api = GithubAPI(username=user)
        api.APT()
    elif choice == "2":
        view_user = input("Enter the Gihub username to view events: ")
        api = GithubAPI(view_user=view_user)
        api.view_events()
    elif choice == "3":
        print("Exiting the program. Goodbye!")
        running = False