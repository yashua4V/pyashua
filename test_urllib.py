#!/usr/bin/python3 
import urllib
import re
import sys
value={}
value['q']=sys.argv[1]
print(value)
print(urllib.urlencode(value))
date=re.findall('q=(.*)',urllib.parse.urlencode(value))[0]
print(date)
