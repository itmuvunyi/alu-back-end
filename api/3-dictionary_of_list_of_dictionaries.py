#!/usr/bin/python3
import json
import requests

if __name__ == "__main__":
    # API endpoints
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch users and tasks data
    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    all_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        user_tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos if task.get("userId") == user_id
        ]
        all_tasks[user_id] = user_tasks

    # Write the result to a JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)
