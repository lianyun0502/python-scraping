import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.dcard.tw/f")
if r.status_code==200:
    #print(r.text)
    soup = BeautifulSoup(r.text,'html.parser')
    titles = soup.find_all('h2')
    link = soup.find_all('a',class_='tgn9uw-3 ebwnQU')
    for t, l in zip(titles, link):
        print(t.string)
        print('https://www.dcard.tw'+l.get('href'))