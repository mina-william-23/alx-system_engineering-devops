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
    )
    try:
        res = req.json()
        return res.get('data').get('subscribers')
    except Exception as e:
        return 0
