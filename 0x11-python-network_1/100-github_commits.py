#!/usr/bin/python3
"""lists 10 commits (from the most recent to oldest) of a repository by a user
prints all commits by: `<sha>: <author name>` (one by line)
"""

import sys
import requests


if __name__ == '__main__':
    owner = sys.argv[1]
    repo = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(repo, owner)
    request = requests.get(url)
    response = request.json()

    for commit in response[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
