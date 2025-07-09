#!/usr/bin/python3
"""
Fetches TODO tasks for all users from a public API
and exports the data into a JSON file.

This script retrieves data from https://jsonplaceholder.typicode.com,
organizes tasks by user, and saves them in 'todo_all_employees.json'.
"""

import json
from typing import Any, Dict, List

import requests


def fetch_data(url: str) -> List[Dict[str, Any]]:
    """
    Fetches JSON data from a given URL.

    Args:
        url (str): The API endpoint to request.

    Returns:
        List[Dict[str, Any]]: Parsed JSON data as a list of dictionaries.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return []


def export_tasks_to_json(
    filename: str, data: Dict[int, List[Dict[str, Any]]]
) -> None:
    """
    Exports the provided data to a JSON file.

    Args:
        filename (str): The name of the file to save the data.
        data (Dict[int, List[Dict[str, Any]]]): The data to export.
    """
    try:
        with open(filename, "w") as jsonfile:
            json.dump(data, jsonfile)
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")


def main() -> None:
    """
    Main function to fetch users and todos, process them, and export as JSON.
    """
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users = fetch_data(users_url)
    todos = fetch_data(todos_url)

    all_tasks: Dict[int, List[Dict[str, Any]]] = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        user_tasks = [
            {
                "username": username,
                "task": todo.get("title"),
                "completed": todo.get("completed"),
            }
            for todo in todos
            if todo.get("userId") == user_id
        ]

        all_tasks[user_id] = user_tasks

    export_tasks_to_json("todo_all_employees.json", all_tasks)


if __name__ == "__main__":
    main()
