import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import urllib

url = 'https://www.ptt.cc/bbs/home-sale/index.html'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
req = Request(url=url, headers=headers)
response = urlopen(req)
BS = BeautifulSoup(response.read(),'html.parser')

# response = requests.get(url)
# print(response.headers)
# BS = BeautifulSoup(response.text,'html.parser')

# print(BS.prettify())
# print(BS.div.a)

BS_list = str(BS).split('\n')
print(BS_list)


title_list = []
for i in range(len(BS_list)):
    if '<div class="title">' in BS_list[i]:
        line = BS_list[i+1].strip().split('>')
        if len(line) <= 1:
            continue
        title = line[1].replace('</a','')
        title_list.append(title)

for title in title_list:
    print(title)

print('------------------')
title_list_bs = BS.find_all('div',class_='title')
# print(title_list_bs)
for title in title_list_bs:
    print(title.text.strip())

