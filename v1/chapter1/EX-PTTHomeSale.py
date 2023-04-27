import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/home-sale/index.html'
response = requests.get(url)
BS = BeautifulSoup(response.text,'html.parser')
BS_list = str(BS).split('\n')
print(BS_list)
# print(BS.prettify())
# print(BS.div.a)

title_list = []
for i in range(len(BS_list)):
    if '<div class="title">' in BS_list[i]:
        line = BS_list[i+1].strip().split('>')
        title = line[1].replace('</a','')
        title_list.append(title)

for title in title_list:
    print(title)

print('------------------')
title_list_bs = BS.find_all('div',class_='title')
# print(title_list_bs)
for title in title_list_bs:
    print(title.text.strip())

