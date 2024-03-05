#!/usr/bin/python3
"""AdvancedAPI"""
import requests


def top_ten(subreddit):
    """Returns the top 10 hotest posts for a given subreddit"""
    base_url = 'https://www.reddit.com'
    query = 'r/{}/hot.json'.format(subreddit)
    headers = {
        "User-Agent": "random user"
    }
    params = {
        "limit": 10
    }
    req = requests.get(
        url='{}/{}'.format(base_url, query),
        headers=headers,
        params=params,
        allow_redirects=False
    )
    # if req.status_code != 200:
    #    print('None')
    # else:
    res = req.json().get('data').get('children')
    if res:
        cnt = 0
        for children in res:
            title = children.get('data').get('title')
            if title:
                print(title)
            else:
                break
            cnt += 1
            if cnt == 10:
                break
    else:
        print('None')
