#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys import argv


def export_csv(user_id):
    """export data to csv"""
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(url + "/users/{}".format(user_id)).json()
    todos = requests.get(url + "/todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w") as csv_file:
        for task in todos:
            csv_file.write('"{}","{}","{}","{}"\n'.format(
                user_id,
                user.get("username"),
                task.get("completed"),
                task.get("title")))


if __name__ == "__main__":
    export_csv(argv[1])
