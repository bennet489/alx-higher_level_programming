#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status
"""

import requests


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    request = requests.get(url)
    text = request.text

    print('Body response:')
    print('\t- type: {}'.format(type(text)))
    print('\t- content: {}'.format(text))
