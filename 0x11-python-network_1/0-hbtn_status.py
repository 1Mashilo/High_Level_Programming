#!/usr/bin/python3

"""
This script fetches the status of https://alx-intranet.hbtn.io/status using the urllib package.

The script sends a GET request to the specified URL and retrieves the response. It then prints the following information:
- The type of the response body
- The content of the response body
- The UTF-8 decoded content of the response body
"""

import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    body = response.read()

print("Body response:")
print(f"\t- type: {type(body)}")
print(f"\t- content: {body}")
print(f"\t- utf8 content: {body.decode('utf-8')}")