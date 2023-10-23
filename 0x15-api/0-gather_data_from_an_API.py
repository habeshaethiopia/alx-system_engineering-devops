#!/usr/bin/python3
"""INtro to restfulapi"""
import requests
import urllib
from sys import argv
import json


if __name__ == "__main__":
    result = []
    count = 0
    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos/").json()
    response2 = json.loads(
        (
            urllib.request.urlopen(
                f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
            )
            .read()
            .decode("utf-8")
        )
    )
    for i in response:
        if i.get("userId") == int(argv[1]):
            result.append(i)
            if i.get("completed") is True:
                count += 1
    print(
        f"Employee {response2.get('name')} is done with tasks\
        ({count}/{len(result)})"
    )
    for i in result:
        if i.get("completed") is True:
            print("\t {}".format(i.get("title")))
