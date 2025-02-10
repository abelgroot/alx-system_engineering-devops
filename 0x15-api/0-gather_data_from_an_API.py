#!/usr/bin/python3

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee details
    employee_url = f"{base_url}/users/{employee_id}"
    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        print(f"Error: Unable to fetch data for employee ID {employee_id}")
        return
    employee_data = employee_response.json()
    employee_name = employee_data.get("name")

    # Fetch TODO list for the employee
    todo_url = f"{base_url}/users/{employee_id}/todos"
    todo_response = requests.get(todo_url)
    if todo_response.status_code != 200:
        print(f"Error: Unable to fetch TODO \
              list for employee ID {employee_id}")
        return
    todo_list = todo_response.json()

    # Calculate total and completed tasks
    total_tasks = len(todo_list)
    completed_tasks = [task for task in todo_list if task.get("completed")]
    num_completed_tasks = len(completed_tasks)

    # Print the first line with employee name and task progress
    print(f"Employee {employee_name} is done \
          with tasks({num_completed_tasks}/{total_tasks}):")

    # Print the titles of completed tasks
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


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
