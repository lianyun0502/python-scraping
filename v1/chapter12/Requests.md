

# Requests
==================
Requests: https://requests.readthedocs.io/en/latest/
## Requests的安裝
```
pip install requests
```
requests庫7個主要方法

|方法	|說明|
|---|---|
|requests.request()	|構造一個請求，支撐以下各方法的基礎方法|
|requests.get()	|獲取HTML網頁的主要方法，對應HTTP的GET|
|requests.head()	|獲取HTML網頁頭信息的方法，對應HTTP的HEAD|
|requests.post()	|向HTML網頁提交POST請求的方法，對應HTTP的POST|
|requests.put()	|向HTML網頁提交PUT請求的方法，對應HTTP的PUT|
|requests.patch()	|向HTML網頁提交局部修改請求，對應HTTP的PATCH|
|requests.delete()	|向HTML網頁提交刪除請求，對應HTTP的DELETE|


理解requests庫的異常

|異常類別	|說明|
|---|---|
|requests.ConnectionError	|網路連接錯誤異常，如DNS查詢失敗、拒絕連接等|
|requests.HTTPError	|HTTP錯誤異常|
|requests.URLRequired	|URL缺失錯誤|
|requests.TooManyRedirects	|超過最大重定向次數，產生重定向錯誤|
|requests.ConnectTimeout	|連接遠端伺服器超時異常|
|requests.Timeout	|請求URL超時，產生超時異常|

get()方法的使用

```python
response = requests.get(url, params=None, **kwargs)
```

```python
import requests

url = 'https://requests.readthedocs.io/en/latest/'
response = requests.get(url)
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)
```
列出幾個response重要的屬性：

|屬性	|說明|
|---|---|
|   response.status_code	|HTTP請求返回狀態碼，200表示成功|
|   response.text	|HTTP響應的字符串形式，即，url對應的頁面內容|
|   response.encoding	|從HTTP　header中猜測的響應內容的編碼方式|
|   response.apparent_encoding	|從內容中分析響應內容的編碼方式(備選編碼方式)|
|   response.content	|HTTP響應內容的二進位形式|

post()方法的使用

```python
response = requests.post(url, data=None, json=None, **kwargs)
```

```python   
import requests

url = 'http://httpbin.org/post'
data = {'key':'value'}
r = requests.post(url, data=data)
print(r.text)
```

put()方法的使用

```python
response = requests.put(url, data=None, **kwargs)
```

```python
import requests

url = 'http://httpbin.org/put'
data = {'key':'value'}
r = requests.put(url, data=data)
print(r.text)
```

delete()方法的使用

```python
response = requests.delete(url, **kwargs)
```

```python
import requests

url = 'http://httpbin.org/delete'
r = requests.delete(url)
print(r.text)
```