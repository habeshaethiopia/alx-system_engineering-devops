#!/usr/bin/python3
"""the recursive function"""
import requests


def recurse(subreddit, hot_list=[]):
    """recursive function"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    r = requests.get(url, headers=headers, params={"limit": 100})
    if r.status_code == 200:
        for post in r.json().get("data").get("children"):
            hot_list.append(post.get("data").get("title"))
        after = r.json().get("data").get("after")
        if after is not None:
            return recurse(subreddit, hot_list)
        else:
            return hot_list
    else:
        return None
