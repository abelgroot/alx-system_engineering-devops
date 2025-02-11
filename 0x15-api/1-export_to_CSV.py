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

    username = user.get("username")
    filename = f"{employee_id}.csv"

    with open(filename, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)
    export_to_csv(int(sys.argv[1]))
