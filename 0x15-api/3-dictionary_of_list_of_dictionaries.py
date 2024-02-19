#!/usr/bin/python3
"""export all todos of users data to json"""
import json
import requests
from sys import argv


def export_json():
    """export all todos of users data to json"""
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(url + "/users").json()
    data = {}

    for user in users:
        user_username = user.get("username")
        user_id = user.get("id")
        user_todos = requests.get(url + "/todos", params={"userId": user_id})
        user_todos = user_todos.json()

        tasks_list = []
        data[user_id] = tasks_list

        for task in user_todos:
            t = {"username": user_username,
                 "task": task.get('title'),
                 "completed": task.get('completed')}
            tasks_list.append(t)

    file_name = "todo_all_employees.json"
    with open(file_name, "w") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    export_json()
