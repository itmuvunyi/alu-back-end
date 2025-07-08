#!/usr/bin/python3
"""
This script fetches an employee's TODO list progress from a REST API
and exports the data to a JSON file.
"""

import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    user_url = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch user data
    user_response = requests.get(user_url, timeout=10)
    if user_response.status_code != 200:
        print("Employee not found.")
        sys.exit(1)

    employee_username = user_response.json().get("username")

    # Fetch TODOs for the employee only
    todos_response = requests.get(
        todos_url,
        params={"userId": employee_id},
        timeout=10
    )
    if todos_response.status_code != 200:
        print("Failed to fetch TODOs.")
        sys.exit(1)

    todos = todos_response.json()

    # Build JSON data structure
    tasks_list = []
    for task in todos:
        task_info = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee_username
        }
        tasks_list.append(task_info)

    data = {str(employee_id): tasks_list}

    # Write to JSON file
    json_filename = f"{employee_id}.json"
    with open(json_filename, mode="w") as json_file:
        json.dump(data, json_file, indent=4)
