import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('eric', '123')
r = requests.get(url="https://pythonscraping.com/pages/auth/login.php", auth=auth)
print(r.text)