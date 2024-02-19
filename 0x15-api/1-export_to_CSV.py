#!/usr/bin/python3
"""Gather data from an API"""
import csv
import requests
from sys import argv


def export_csv(user_id):
    """export data to csv"""
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(url + "/users/{}".format(user_id)).json()
    todos = requests.get(url + "/todos", params={"userId": user_id}).json()

    employee_username = user.get("username")
    with open("{}.csv".format(user_id), "w") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            row = (user_id, employee_username,
                   task.get('completed'), task.get('title'))
            writer.writerow(row)


if __name__ == "__main__":
    export_csv(argv[1])
