#!/usr/bin/python3
"""
This script takes in a URL, sends a requeest to it and displays the value of
the variable X-Request-Id in the response header
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <URL>")
        sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
