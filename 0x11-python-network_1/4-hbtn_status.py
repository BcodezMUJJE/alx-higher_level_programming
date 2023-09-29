#!/usr/bin/python3

"""
This script fetches the URL https://alx-intranet.hbtn.io/status using the requests package
and displays the body of the response in a specific format.
"""

import requests

def fetch_status():
    """
    Fetches the status URL and displays the response body in a specific format.
    """
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)

    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)

if __name__ == "__main__":
    fetch_status()
