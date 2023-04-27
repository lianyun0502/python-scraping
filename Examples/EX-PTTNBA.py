import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/NBA/index.html'
deleted = BeautifulSoup("<a href = 'Deleted'>本文已刪除</a>",'html.parser').a

reqs=requests.get(url)
if reqs.status_code == requests.codes.ok:
    reqs.encoding = 'utf8'
    soup = BeautifulSoup(reqs.text, 'html.parser')
    tag_divs = soup.find_all('div',class_='r-ent')
    for tag in tag_divs:
        tag_a = tag.find('a') or deleted
        print(tag_a['href'])
        print(tag_a.text)
        print(tag.find('div',class_='author').string)
else:
    print('HTTP請求錯誤...'+url)