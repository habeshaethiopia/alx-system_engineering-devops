#!/usr/bin/python3
"""export to scv file"""
import json
import requests
import sys
import urllib


if __name__ == "__main__":
    result = []
    count = 0
    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos/").json()
    response2 = json.loads(
        (
            urllib.request.urlopen(
                f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
            )
            .read()
            .decode("utf-8")
        )
    )
    for i in response:
        if i.get("userId") == int(sys.argv[1]):
            result.append(i)
            if i.get("completed") is True:
                count += 1
    name = response2.get("username")
    with open("{}.csv".format(sys.argv[1]), "w") as f:
        for i in result:
            f.write(
                '"{}","{}","{}","{}"\n'.format(
                    sys.argv[1], name, i.get("completed"), i.get("title")
                )
            )
