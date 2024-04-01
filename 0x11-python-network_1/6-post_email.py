#!/usr/bin/python3

"""
Sends a POST request to a URL with an email address as data.

This script takes a URL and an email address as input, constructs a POST request with the email
as payload data, sends the request, and displays the response body.

Args:
    url (str): The target URL for the POST request.
    email (str): The email address to send in the 'email' parameter.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)

    print(response.text)