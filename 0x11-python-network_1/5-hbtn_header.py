#!/usr/bin/python3
"""
Takes in a URL, sends a request using requests, and displays
the value of the X-Request-Id variable found in the response header
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    # Send a GET request
    response = requests.get(url)
    # Access headers and print the X-Request-Id value
    print(response.headers.get("X-Request-Id"))
