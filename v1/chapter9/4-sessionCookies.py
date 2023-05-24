import requests

session = requests.Session()
param = {'username': 'username', 'password': 'password'}
s = session.post("https://pythonscraping.com/pages/cookies/welcome.php", data=param)
print("Cookie is set to:")
print(s.cookies.get_dict())
print("-----------")
print("Going to profile page...")
s = session.get("https://pythonscraping.com/pages/cookies/profile.php")
print(s.text)

s = session.get("https://pythonscraping.com/pages/cookies/profile.php")
print(s.text)