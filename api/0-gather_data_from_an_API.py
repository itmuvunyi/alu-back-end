#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    # Validate argument count
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]

    # Validate that the input is an integer
    if not employee_id.isdigit():
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Convert to int
    employee_id = int(employee_id)

    # API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch employee data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Employee not found.")
        sys.exit(1)
    employee_name = user_response.json().get("name")

    # Fetch todos data
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Count tasks
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    # Display progress
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
