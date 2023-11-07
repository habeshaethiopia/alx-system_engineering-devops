#!/usr/bin/python3
"""Top Ten"""
import requests


def top_ten(subreddit):
    """the top ten"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    r = requests.get(url, headers=headers, params={"limit": 10})
    if r.status_code == 200:
        for post in r.json().get("data").get("children"):
            print(post.get("data").get("title"))
    else:
        print(None)
