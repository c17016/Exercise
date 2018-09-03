#!/usr/bin/python3

import requests, bs4
res = requests.get("https://www.youtube.com/")
res.raise_for_status()
no_starch_soup = bs4.BeautifulSoup(res.text)
print(no_starch_soup)