#!/bin/bash
# This script takes in a URL, sends a request to that URL and displays the size of body of the response
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
