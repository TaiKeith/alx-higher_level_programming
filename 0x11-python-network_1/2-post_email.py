#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
"""
import urllib.request
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    data = f"email={email}".encode('utf-8')

    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')
        print(body)
