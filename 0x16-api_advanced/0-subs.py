#!/usr/bin/python3
"""returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.json().get("data").get("subscribers")
    else:
        return 0
