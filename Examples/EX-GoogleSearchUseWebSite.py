import requests
from bs4 import BeautifulSoup
import urllib.parse

googleUrl = 'https://www.google.com.tw/search'

my_params = {'q': '寒流'}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
r = requests.get(googleUrl, params=my_params, headers=headers)

if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, "html.parser")
    # print(r.text)

    itemsTitle = soup.select('div.rc > div.yuRUbf > a > h3')
    itemsLink = soup.select('div.rc > div.yuRUbf > a')

    for t, l in zip(itemsTitle, itemsLink):
        print("標題:", t.text)
        print("網址:", urllib.parse.unquote(l.get('href')))