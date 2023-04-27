import requests
from bs4 import BeautifulSoup

url = 'https://buzzorange.com/techorange/'

my_params = ['智慧製造', 'fintech', '數位行銷']

for i in range(len(my_params)):
    use_params = {'s': my_params[i]}
    resp = requests.get(url + "?s=" + my_params[i])
    soup = BeautifulSoup(resp.text, 'html.parser')

    techOrange_title = soup.find_all('h4')
    print('\ntechOrange' + my_params[i] + '熱門標題：\n')
    for index, item in enumerate(techOrange_title[:10]):
        print("{0:2d}. {1}".format(index + 1, item.text.strip()))