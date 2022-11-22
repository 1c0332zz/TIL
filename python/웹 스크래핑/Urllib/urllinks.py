# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
import collections
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

collections.Callable = collections.abc.Callable
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urllib.request.urlopen(url, context=ctx).read()
# 못생긴 html을 넘길테니 soup에서 알아서 읽어줘
soup = BeautifulSoup(html, "html.parser")

# <a>태그를 전부 가져와
tags = soup("a")
for tag in tags:
    print(tag.get("href", None))
