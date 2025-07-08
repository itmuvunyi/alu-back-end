#!/usr/bin/python3
"""
This script fetches an employee's TODO list progress from a REST API
and exports the data to a CSV file.
"""

import csv
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
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch user data
    user_response = requests.get(user_url, timeout=10)
    if user_response.status_code != 200:
        print("Employee not found.")
        sys.exit(1)

    employee_username = user_response.json().get("username")

    # Fetch TODOs for that user only
    todos_response = requests.get(
        todos_url, params={"userId": employee_id}, timeout=10
    )
    todos = todos_response.json()

    # Write to CSV file
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                employee_username,
                task.get("completed"),
                task.get("title")
            ])
