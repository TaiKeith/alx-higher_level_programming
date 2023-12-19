#!/usr/bin/python3
"""
This script takes in a URL, sends a request to it and displays the body of the
response
"""
import urllib.request
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <URL>")
        sys.exit(1)

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
