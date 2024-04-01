#!/usr/bin/python3

"""
Fetches content from a URL and handles HTTPError exceptions.

This script attempts to fetch the content from a provided URL.
If a successful response is
received, the decoded content is printed. If an HTTPError occurs,
the error code is printed.

Args:
    url (str): The URL to fetch content from.
"""

import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
