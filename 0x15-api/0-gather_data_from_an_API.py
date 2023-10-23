#!/usr/bin/python3
"""INtro to restfulapi"""
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
    print(
        "Employee {} is done with tasks({}/{}):".format(
            response2.get("name"), count, len(result)
        )
    )
    for i in result:
        if i.get("completed") is True:
            print("\t {}".format(i.get("title")))
