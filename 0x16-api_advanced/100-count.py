#!/usr/bin/python3
"""the recursive word count"""
import requests

def count_words(subreddit, word_list):
    word_counts = {}
    word_list = [word.lower() for word in word_list]


    count_words_recursive(subreddit, word_list, None, word_counts)

    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_word_counts:
        print("{}: {}".format(word, count))

def count_words_recursive(subreddit, word_list, after, word_counts):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    params = {"limit": 100, "after": after}
    r = requests.get(url, headers=headers, params=params)
    if r.status_code == 200:
        data = r.json().get("data")
        for post in data.get("children"):
            title_words = post.get("data").get("title").lower().split()
            for word in title_words:
                if word in word_list:
                    word_counts[word] = word_counts.get(word, 0) + 1
        after = data.get("after")
        if after is not None:
            count_words_recursive(subreddit, word_list, after, word_counts)