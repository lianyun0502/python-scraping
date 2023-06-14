import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
data = {'from': '/bbs/Gossiping/index.html', 'yes': 'yes'}

response = requests.post(url, data=data)

print(response.text)