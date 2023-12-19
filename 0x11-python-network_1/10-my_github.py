#!/usr/bin/python3
"""
This script takes my GitHub credentials (username and password) and uses
the GitHub API to display my id
Usage:
    1st arg - username
    2nd arg - password
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    auth = HTTPBasicAuth(username, password)
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
