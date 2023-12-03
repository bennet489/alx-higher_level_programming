#!/usr/bin/python3
"""takes a GitHub credentials (username and password) and uses the GitHub API
to display the id
"""

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    request = requests.get(url, auth=auth)

    print(request.json().get("id"))
