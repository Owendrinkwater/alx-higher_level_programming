#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to it, and displays
the value of the X-Request-Id variable found in the header.
"""

import urllib.request
import sys

if __name__ == "__main__":
    # Get the URL from the first command-line argument
    url = sys.argv[1]

    # Send the request using a with statement
    with urllib.request.urlopen(url) as response:
        # Get the headers
        headers = response.info()

        # Print the X-Request-Id value from the headers
        print(headers.get("X-Request-Id"))
