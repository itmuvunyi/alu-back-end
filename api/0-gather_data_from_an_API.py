#!/usr/bin/python3
"""
This script retrieves and displays an employee's TODO list progress
using a REST API from https://jsonplaceholder.typicode.com.
"""

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

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Employee not found.")
        sys.exit(1)

    employee_name = user_response.json().get("name")

    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed") is True]
    number_of_done_tasks = len(done_tasks)

    msg = "Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks
    )
    print(msg)

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
