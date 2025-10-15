#!/usr/bin/python3
"""Uses GitHub API to display the authenticated user's id"""

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]  # Personal access token

    url = "https://api.github.com/user"

    r = requests.get(url, auth=(username, token))

    try:
        user_data = r.json()
        print(user_data.get("id"))
    except ValueError:
        print(None)
