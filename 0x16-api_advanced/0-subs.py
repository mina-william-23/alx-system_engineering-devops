 #!/usr/bin/python3
"""AdvancedAPI"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of suscriber for a given subreddit"""
    base_url = 'https://www.reddit.com'
    query = 'r/{}/about.json'.format(subreddit)
    headers = {
        "User-Agent": "linux:hbtn.advanced.api (by /u/koeusiss)"
    }
    req = requests.get(
        url='{}/{}'.format(base_url, query),
        headers=headers,
    )
    # if req.status_code != 200:
    #    return 0
    try :
        res = req.json()
        return res.get('data').get('subscribers')
    except Exception as e:
        return 0
