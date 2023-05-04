import requests
from bs4 import BeautifulSoup
import urllib.parse

googleUrl = 'https://www.google.com.tw/search'

my_params = {'q': 'python'}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
r = requests.get(googleUrl, params=my_params, headers=headers)

if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, "html.parser")
    # print(soup.prettify())

    titles = soup.select('div.yuRUbf')
    describes = soup.select('div.VwiC3b')
    for t, d in zip(titles, describes):
        print("=====================================")
        print("標題:", t.select('a > h3')[0].text)
        print("網址:", t.a.get('href'))
        describe = d.select('span')
        if len(describe) == 0:
            continue
        elif len(describe) == 1:
            print("描述:", describe[0].text)
        else:
            print("日期:", describe[1].text)
            print("描述:", describe[2].text)

