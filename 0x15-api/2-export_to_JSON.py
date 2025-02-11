#!/usr/bin/python3
"""
Python script to fetch an employee's TODO list progress from a REST API
and export it to a JSON file.
"""
import json
import requests
import sys


def fetch_employee_data(employee_id):
    """Fetch employee and TODO list data from the API."""
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f"{url}users/{employee_id}").json()
    todos = requests.get(f"{url}todos", params={"userId": employee_id}).json()

    if not user or "id" not in user:
        print("Invalid employee ID")
        return None, None

    return user, todos


def export_to_json(user, todos):
    """Export TODO list data for a given employee to JSON."""
    user_id = user.get("id")
    username = user.get("username")
    filename = f"{user_id}.json"

    # Prepare the data in the required JSON format
    tasks = [{"task": task.get("title"),
              "completed": task.get("completed"),
              "username": username} for task in todos]
    data = {str(user_id): tasks}

    # Write the data to a JSON file
    with open(filename, mode="w") as jsonfile:
        json.dump(data, jsonfile, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user, todos = fetch_employee_data(employee_id)

    if user and todos:
        export_to_json(user, todos)
