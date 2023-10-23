#!/usr/bin/python3
"""export to all the result to json file"""
import json
import requests
import urllib


if __name__ == "__main__":
    result = []

    response = requests\
        .get("https://jsonplaceholder.typicode.com/todos/").json()
    response2 = json.loads(
        (
            urllib.request.urlopen(
                f"https://jsonplaceholder.typicode.com/users/")
            .read()
            .decode("utf-8")
        )
    )

    with open("todo_all_employees.json", "w") as f:
        file = {}
        for user in response2:
            name = user.get("username")
            file_li = []
            for i in response:
                if user.get("id") == i.get("userId"):
                    file_li.append(
                        {
                            "task": i.get("title"),
                            "completed": i.get("completed"),
                            "username": name,
                        }
                    )
            file[user.get("id")] = file_li
        json.dump(file, f)
