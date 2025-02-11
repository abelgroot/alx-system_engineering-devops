#!/usr/bin/python3
"""
Python script to fetch all employees' TODO lists from a REST API
and export the data to a JSON file.
"""
import json
import requests


def fetch_all_employees_data():
    """Fetch all employees and their TODO lists from the API."""
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(f"{url}users").json()
    todos = requests.get(f"{url}todos").json()

    # Create a dictionary to store tasks for all employees
    all_employees_data = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        user_tasks = [task for task in todos if task.get("userId") == user_id]

        # Format tasks for the current user
        tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed"),
            }
            for task in user_tasks
        ]

        # Add the user's tasks to the dictionary
        all_employees_data[str(user_id)] = tasks

    return all_employees_data


def export_to_json(data):
    """Export all employees' TODO lists to a JSON file."""
    filename = "todo_all_employees.json"
    with open(filename, mode="w") as jsonfile:
        json.dump(data, jsonfile, indent=4)


if __name__ == "__main__":
    # Fetch all employees' data
    all_employees_data = fetch_all_employees_data()

    # Export the data to a JSON file
    export_to_json(all_employees_data)
