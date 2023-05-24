import requests
from bs4 import BeautifulSoup

session = requests.session()

my_data = {'from': '/bbs/Gossiping/index.html',
           'yes': 'yes'}

r = session.post("https://www.ptt.cc/ask/over18", data=my_data)

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
response = session.get(url)
print(response.text)

# while (True):
#     r2 = session.get(url)
#     if r2.status_code == 200:
#         soup = BeautifulSoup(r2.text, 'html.parser')
#         titles = soup.find_all('div', class_='title')
#         link = soup.select('div.title > a')
#         newUrl = "https://www.ptt.cc" + soup.select('div.btn-group.btn-group-paging > a')[1].get('href')
#         for t, l in zip(titles, link):
#             if "川普" not in t.text or "Re" in t.text:
#                 continue
#             print(t.text)
#             # print("https://www.ptt.cc"+l.get('href'))
#             r3 = request.get("https://www.ptt.cc" + l.get('href'))
#             soup3 = BeautifulSoup(r3.text, 'html.parser')
#
#             content = soup3.select_one('div#main-content').text
#
#             target_content = u'※ 發信站: 批踢踢實業坊(ptt.cc),'
#             content = content.split(target_content)[0]
#
#             date_content = soup3.select('span.article-meta-value')[3].text
#             content = content.split(date_content)[1]
#
#             main_content = content.replace('\n', '  ').replace('\t', '  ')
#             print(main_content)
#         url = newUrl