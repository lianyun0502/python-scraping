import requests

params = {'firstname': 'Ryan', 'lastname': 'Mitchell'}
r = requests.post("https://pythonscraping.com/pages/processing.php", params=params)
print(r.text)