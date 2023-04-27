import requests
from bs4 import BeautifulSoup
import os


def pttImage(keyword, count):
    pics = []
    picCount = 0

    r = requests.Session()
    payload = {
        "from": "/bbs/Beauty/index.html",
        "yes": "yes"
    }
    r.post("https://www.ptt.cc/ask/over18?from=%2Fbbs%2FBeauty%2Findex.html", payload)

    url = "https://www.ptt.cc/bbs/Beauty/index.html"
    os.makedirs(keyword)

    while True:
        title = []
        titleUrl = []
        r2 = r.get(url)
        soup = BeautifulSoup(r2.text, "html.parser")

        sel = soup.select("div.title a")  # 標題
        u = soup.select("div.btn-group.btn-group-paging a")  # a標籤
        url = "https://www.ptt.cc" + u[1]["href"]  # 上一頁的網址

        for s in sel:  #
            if keyword in s.text:
                # 帥哥 正妹 新垣結衣"
                title.append(s.text)
                titleUrl.append(s["href"])
                # print(s["href"],s.text)

        for i in range(len(titleUrl)):
            url2 = "https://www.ptt.cc" + titleUrl[i]
            r3 = r.get(url2)
            soup = BeautifulSoup(r3.text, "html.parser")
            sel2 = soup.select("a")

            for s in sel2:
                picUrl = s["href"]
                if "jpg" in picUrl or "gif" in picUrl or "png" in picUrl:
                    pics.append(picUrl)
                    resp2 = r.get(picUrl)
                    if resp2.status_code == 200:
                        with open(keyword + '/' + str(pics.index(picUrl) + 1) + picUrl[-4:], 'wb') as f:
                            for chunk in resp2:
                                f.write(chunk)
                            picCount = picCount + 1
                if picCount == count:
                    print("--------------------------------------------")
                    print("已經都抓完囉")
                    return


while True:
    keyword = input("請輸入想搜尋誰的照片(或按q結束程式):")
    if keyword == "q" or keyword == "Q":
        print("程式結束")
        break
    else:
        count = eval(input("請輸入想搜尋幾張:"))
        pttImage(keyword, count)