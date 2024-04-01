#!/usr/bin/python3
import urllib.request
import sys


if __name__ == "__main__":
    """
    Sends a request to a URL and prints the value of the 'X-Request-Id' header in the response.

    Args:
        url (str): The URL to send the request to.

    Returns:
        None
    """
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        header = response.getheader('X-Request-Id')
        print(header)