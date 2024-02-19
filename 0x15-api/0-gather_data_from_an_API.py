#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys import argv


def gather_data(user_id):
    """Gather data from an API"""
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(url + "/users/{}".format(user_id)).json()
    todos = requests.get(url + "/todos", params={"userId": user_id}).json()

    completed_tasks = []
    for task in todos:
        if task.get("completed") is True:
            completed_tasks.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"),
        len(completed_tasks),
        len(todos)))

    for task in completed_tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    gather_data(argv[1])
