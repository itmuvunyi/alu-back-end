#!/usr/bin/python3
"""
Fetches tasks for all employees from a REST API and exports them to
a JSON file.
"""

import json
import requests


def fetch_data(url):
    """
    Fetch JSON data from the given URL.
    """
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response.json()


def main():
    """
    Fetches employee and task data from an API and writes it to a JSON file.
    """
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users = fetch_data(users_url)
    todos = fetch_data(todos_url)

    all_tasks = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        user_tasks = []

        for todo in todos:
            if todo.get("userId") == user_id:
                task_data = {
                    "username": username,
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                }
                user_tasks.append(task_data)

        all_tasks[user_id] = user_tasks

    with open("todo_all_employees.json", "w", encoding="utf-8") as jsonfile:
        json.dump(all_tasks, jsonfile)


if __name__ == "__main__":
    main()
