import requests
from bs4 import BeautifulSoup
import urllib.parse

r = requests.get("https://tw.yahoo.com")

if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text,"html.parser")
    #print(r.text)
    stories = soup.find_all('a',class_="Fz(16px) LineClamp(1,20px) Fw(700) Td(n) Td(u):h C(#324fe1) V(h) active_V(v)")
    for s in stories:
        print("標題:", s.text)
        print("網址:", urllib.parse.unquote(s.get('href')))