#!/usr/bin/python3
"""
This script retrieves and displays the
TODO list progress for a given employee
ID using the JSONPlaceholder API. It uses
urllib to make HTTP requests.
"""

import json
import sys
import urllib.request


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"

    try:
        # Fetch employee details
        employee_url = f"{base_url}/users/{employee_id}"
        with urllib.request.urlopen(employee_url) as response:
            employee_data = json.loads(response.read().decode('utf-8'))

        if not employee_data:
            print(f"Error: No data found for employee ID {employee_id}")
            return

        employee_name = employee_data.get("name")

        # Fetch TODO list for the employee
        todo_url = f"{base_url}/users/{employee_id}/todos"
        with urllib.request.urlopen(todo_url) as response:
            todo_list = json.loads(response.read().decode('utf-8'))

        # Calculate total and completed tasks
        total_tasks = len(todo_list)
        completed_tasks = [task for task in todo_list if task.get("completed")]
        num_completed_tasks = len(completed_tasks)

        # Print the first line with employee name and task progress
        # Ensure the static part is exactly 26 characters long
        print(f"Employee {employee_name} is done with\
                 tasks({num_completed_tasks}/{total_tasks}):")

        # Print the titles of completed tasks
        for task in completed_tasks:
            print(f"\t {task.get('title')}")

    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - Unable to fetch\
                 data for employee ID {employee_id}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        if employee_id <= 0:
            raise ValueError("Employee ID must be a positive integer.")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
