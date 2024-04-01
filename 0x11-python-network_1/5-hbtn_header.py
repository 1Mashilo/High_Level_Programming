#!/usr/bin/python3
"""
    Sends a GET request to the specified URL and returns
    the value of the 'X-Request-Id' header.

    Args:
        url (str): The URL to send the GET request to.

    Returns:
        str: The value of import requests

"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
