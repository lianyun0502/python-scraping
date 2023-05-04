import requests

files = {'uploadFile': open(r'C:\Users\eric.li\Desktop\My Github\python-scraping\files\Python-logo.png', 'rb')}
r = requests.post("http://pythonscraping.com/pages/processing2.php", 
                  files=files)

print(r.text)