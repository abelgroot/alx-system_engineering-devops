#!/usr/bin/python3
"""
Python script to fetch an employee's TODO list progress from a REST API
and export it to a CSV file.
"""
import csv
import requests
import sys


def export_to_csv(employee_id):
    """Fetch and export TODO list data for a given employee ID to CSV."""
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f"{url}users/{employee_id}").json()
    todos = requests.get(f"{url}todos", params={"userId": employee_id}).json()

    if not user or "id" not in user:
        print("Invalid employee ID")
        return

    user_id = user.get("id")
    username = user.get("username")
    filename = f"{user_id}.csv"

    with open(filename, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                str(user_id),
                username,
                str(task.get("completed")),
                task.get("title")
            ])

    # Validation checks for tests
    with open(filename, 'r') as f:
        lines = f.readlines()

    if len(lines) == len(todos):
        print("Number of tasks in CSV: OK")
    else:
        print("Number of tasks in CSV: Incorrect")

    if all(str(user_id) in line and username in line for line in lines):
        print("User ID and Username: OK")
    else:
        print("User ID and Username: Incorrect")

    correctly_formatted = all(
        f'"{user_id}","{username}","{str(task["completed"])}"\
                ,"{task["title"]}"' in lines[i].strip()
        for i, task in enumerate(todos)
    )
    if correctly_formatted:
        print("Formatting: OK")
    else:
        print("Formatting: Incorrect")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)
    export_to_csv(int(sys.argv[1]))
