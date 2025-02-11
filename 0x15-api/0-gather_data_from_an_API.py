#!/usr/bin/python3
"""
Python script to fetch an employee's TODO list progress from a REST API.
"""
import requests
import sys


def get_todo_progress(employee_id):
    """Fetch and display TODO list progress for a given employee ID."""
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f"{url}users/{employee_id}").json()
    todos = requests.get(f"{url}todos", params={"userId": employee_id}).json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [task.get("title") for task in todos if task.get("completed")]

    output = "Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), total_tasks
    )
    print(output)

    for task in done_tasks:
        print(f"\t {task}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    get_todo_progress(int(sys.argv[1]))
