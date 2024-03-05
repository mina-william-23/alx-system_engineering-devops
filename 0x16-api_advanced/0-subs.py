#!/usr/bin/python3
"""AdvancedAPI"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of suscribers"""
    base_url = 'https://www.reddit.com'
    query = 'r/{}/about.json'.format(subreddit)
    headers = {
        "User-Agent": "random user"
    }
    req = requests.get(
        url='{}/{}'.format(base_url, query),
        headers=headers,
        # allow_redirects=False
    )

    res = req.json().get('data', None).get('subscribers', None)
    return res if int(res) else 0
