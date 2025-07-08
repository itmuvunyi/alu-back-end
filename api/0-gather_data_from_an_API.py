#!/usr/bin/python3
"""
Fetch and display TODO‑list progress for a given employee ID.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Get user info
    user_url = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )
    user_response = requests.get(user_url, timeout=10)
    if user_response.status_code != 200:
        print("Employee not found.")
        sys.exit(1)

    employee_name = user_response.json().get("name")

    # Get user's TODOs
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos_response = requests.get(
        todos_url, params={"userId": employee_id}, timeout=10
    )
    todos = todos_response.json()

    # Filter completed tasks
    done_tasks = [task for task in todos if task.get("completed")]
    done_count = len(done_tasks)
    total_tasks = len(todos)

    print(
        f"Employee {employee_name} is done with tasks"
        f"({done_count}/{total_tasks}):"
    )
    for task in done_tasks:
        print(f"\t {task.get('title')}")
