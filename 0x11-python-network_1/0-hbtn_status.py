#!/usr/bin/python3
"""
A script that fetches https://alx-intranet.hbtn.io/status
using urllib and displays the response body in a specific format.
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    # Open the URL using a with statement
    with urllib.request.urlopen(url) as response:
        # Read the entire response body
        body = response.read()

        # Print the required output
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode("utf-8"))
