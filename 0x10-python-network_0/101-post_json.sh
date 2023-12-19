#!/bin/bash
# This script sends a JSON POST  request with the contents of the file
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
