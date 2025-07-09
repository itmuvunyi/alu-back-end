#!/usr/bin/python3
import json
import requests

if __name__ == "__main__":
    # API endpoints
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch users and todos data
    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    # Prepare the data structure
    all_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        # List to hold user's tasks
        user_tasks = []

        for todo in todos:
            if todo.get("userId") == user_id:
                task_data = {
                    "username": username,
                    "task": todo.get("title"),
                    "completed": todo.get("completed")
                }
                user_tasks.append(task_data)

        # Add to the main dictionary
        all_tasks[user_id] = user_tasks

    # Export to JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile)
