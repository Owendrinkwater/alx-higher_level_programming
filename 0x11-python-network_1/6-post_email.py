#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request with the email
as a parameter, and displays the body of the response
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    # Send POST request with email in the body as form data
    response = requests.post(url, data={"email": email})
    # Display response body
    print(response.text)
