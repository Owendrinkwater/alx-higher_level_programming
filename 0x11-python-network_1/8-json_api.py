#!/usr/bin/python3
"""Sends a letter to the search API and prints the result"""

import sys
import requests

if __name__ == "__main__":
    # Get the letter from command-line argument or default to empty string
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}

    try:
        r = requests.post(url, data=data)
        r_json = r.json()  # Convert response to JSON

        if r_json:  # If JSON is not empty
            print("[{}] {}".format(r_json.get("id"), r_json.get("name")))
        else:  # JSON is empty
            print("No result")
    except ValueError:  # JSON decoding failed
        print("Not a valid JSON")
