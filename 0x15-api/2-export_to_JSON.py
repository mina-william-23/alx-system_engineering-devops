#!/usr/bin/python3
"""export data to json"""
import json
import requests
from sys import argv


def export_json(user_id):
    """export data to json"""
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(url + "/users/{}".format(user_id)).json()
    todos = requests.get(url + "/todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as json_file:
        employee_id = user_id
        employee_username = user.get("username")

        tasks_list = []
        data = {employee_id: tasks_list}

        for task in todos:
            t = {"task": task.get('title'),
                 "completed": task.get('completed'),
                 "username": employee_username}
            tasks_list.append(t)
        json.dump(data, json_file)


if __name__ == "__main__":
    export_json(argv[1])
