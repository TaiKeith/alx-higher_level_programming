#!/usr/bin/python3
"""
This script takes in a URL, sends a request to it and displays the value of
the X-Request-Id variable found in the header of the response
"""
import urllib.request
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <URL>")
        sys.exit(1)

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)
