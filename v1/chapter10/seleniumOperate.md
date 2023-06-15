# 1.1 控制瀏覽器視窗大小
在不同的瀏覽器大小下訪問測試站點,對測試頁面截圖並儲存,然後觀察或使用影象比對工具對被測頁面的前端樣式進行評測。比如可以將瀏覽器設定成移動端大小(480x800),然後訪問移動站點,對其樣式進行評估;WebDriver 提供了set_window_size() 方法來設定瀏覽器的大小。
### 例子:

```python
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://192.168.30.180/Uet-Platform/")
#引數數字為畫素點
print("****設定瀏覽器寬480、高800 顯示")
driver.set_window_size(480, 800)
driver.quit()
```

在PC 端執行執行自動化測試指令碼大多的情況下是希望瀏覽器在全螢幕模式下執行,那麼可以使用maximize_window()方法,其用法與set_window_size() 相同,但它不需要傳參。

# 1.2 控制瀏覽器後退和前進
在使用瀏覽器瀏覽網頁的時候,瀏覽器提供了後退和前進按鈕,可以方便的對瀏覽過的網頁之間切換,那麼WebDriver 也提供了對應的back()和forward()方法來模擬後退和前進按鈕。下面通過例子來演示這兩個方法的使用。

### 例子:

```python
from selenium import webdriver
driver = webdriver.Firefox()
#訪問百度首頁
first_url= 'http://www.baidu.com'
print("now access %s" %(first_url))
driver.get(first_url)
#****訪問新聞頁面**
second_url='http://news.baidu.com'
print("now access %s" %(second_url))
driver.get(second_url)
#****返回(後退)到百度首頁
print("back to %s "%(first_url))
driver.back()
#****前進到新聞頁
print("forward to %s"%(second_url))
driver.forward()
driver.quit()
```
# 1.3 模擬重新整理瀏覽器
有時候需要手動的重新整理(F5)的重新整理頁面

driver.refresh() #****重新整理當前頁面** 

# 2 元素操作 

## 2.1 常用的元素操作

* clear() 清除文字,如果是一個檔案輸入框
* send_keys(*value) 在元素上模擬按鍵輸入
* click() 單擊元素

### 例子:
```python
from selenium import webdriver
import unittest, time, re
driver = webdriver.Firefox()
driver.implicitly_wait(30)
base_url ="http://192.168.30.180/Uet-Platform/masterLogin.action" #30****測試環境**
driver.get(base_url)
driver.find_element_by_id("txtUserName").clear()
driver.find_element_by_id("txtUserName").send_keys("13554797004")
driver.find_element_by_id("txtPassword").clear()
driver.find_element_by_id("txtPassword").send_keys("123123")
driver.find_element_by_link_text(u"登入").click()
driver.switch_to_frame("lj_left")
driver.find_element_by_xpath("//div[@id='left']/table/tbody/tr[6]/td").click()
driver.find_element_by_link_text(u"****使用者單位管理").click()
```

### 說明:
`clear()`方法用於清除文字輸入框中的內容,例如登入框內一般預設會有“賬號”“密碼”等提示資訊用於引導使用者輸入正確的資料,如果直接向輸入框中輸入資料,可能會與輸入框中的提示資訊拼接,本來使用者輸入為“username”,結果與提示資訊拼接為“帳號username”,從而造成輸入資訊的錯誤;這個時候
可以先使用`clear()`方法清除輸入框內的提示資訊再進行輸入。

`send_keys()`方法模擬鍵盤輸入向輸入框裡輸入內容。如上面的例子中通過這個方法向用戶名和密碼框中輸入使用者名稱和密碼。
`click()`方法可以用來單擊一個按鈕,前提是它是可以被點選元素,它與`send_keys()`方法是web 頁面操作中最常用到的兩個方法。其實`click()`方法不僅僅用於點選一個按鈕,還可以單擊任何可以點選文字/圖片連線、複選框、單選框、甚至是下拉框等。

## 2.2 WebElement 介面常用方法 
## 1. submit()
`submit()`方法用於提交表單,這裡特別用於沒提交按鈕的情況,例如搜尋框輸入關鍵字之後的“回車”操作,那麼就可以通過`submit()`來提交搜尋框的內容。
### 例子:
```python
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.youdao.com")
driver.find_element_by_id('query').send_keys('hello')#提交輸入框的內容
driver.find_element_by_id('query').submit()
driver.quit()
```
有些時候`submit()`可以與`click()`方法互換來使用,`submit()`同樣可以提交一個按鈕。

## 2. find_element_by_id()

* size 返回元素的尺寸。
* text 獲取元素的文字。
* get_attribute(name) 獲得屬性值。
* is_displayed() 設定該元素是否使用者可見。
### 例子:

```python
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

#****獲得輸入框的尺寸
size=driver.find_element_by_id('kw').size
print(size)

#****返回百度頁面底部備案資訊
text=driver.find_element_by_id("cp").text
print(text)

#返回元素的屬性值,可以是id、name、type 或元素擁有的其它任意屬性
attribute=driver.find_element_by_id("kw").get_attribute('type')
print(attribute)

#返回元素的結果是否可見,返回結果為True 或False
result=driver.find_element_by_id("kw").is_displayed()
print(result)
driver.quit()
```

### 執行結果:
```
{'width': 526, 'height': 22}
©2014 Baidu 使用百度前必讀京ICP 證030173 號
True
```

### 解析:
執行上面的程式並獲得執行結果:`size` 用於獲取百度輸入框的寬、高。`text` 用於獲得百度底部的備案資訊。`get_attribute()`用於獲百度輸入的`type` 屬性的值。`is_displayed()`用於返回一個元素是否可見,如果可見返回`True`,否則返回`False`。

# 3. ActionChains 類提供的滑鼠操作的常用方法
* perform() 執行所有ActionChains 中儲存的行為
* click_and_hold(element)左鍵點選
* context_click(elem) 右擊
* double_click(elem) 雙擊
* drag_and_drop(source,target) 拖動
* move_to_element(elem) 滑鼠懸停
## 例子1:滑鼠右擊操作

對於`ActionChains` 類下所提供的滑鼠方法與前面學過的`click()`方法有所不同,那麼簡單`context_click()`右鍵點選一個元素。

```python
from selenium import webdriver*
#引入ActionChains 類*
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
driver.get("http://yunpan.360.cn")

#****定位到要右擊的元素**
right_click =driver.find_element_by_id("xx")

#****對定位到的元素執行滑鼠右鍵操作
ActionChains(driver).context_click(right_click).perform()
```

### 說明:
```from selenium.webdriver import ActionChains```
對於`ActionChains` 類下面的方法,在使用之前需要先將模組匯入。
`ActionChains(driver)`呼叫`ActionChains()`方法,在使用將瀏覽器驅動`driver` 作為引數傳入。
`context_click(right_click)` `context_click()`方法用於模擬滑鼠右鍵事件,在呼叫時需要傳入右鍵的元素。
`perform()` 執行所有`ActionChains` 中儲存的行為,可以理解成是對整個操作事件的提交動作。

## 例子2:滑鼠懸停
滑鼠懸停彈出下拉選單也是一個非常見的一個功能設計 

`move_to_element()`方法可以模擬滑鼠懸停的動作,其用法與`context_click()`相同。
### 程式碼實現:
```python
from selenium import webdriver
#引入ActionChains 類
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()driver.get("http://www.baidu.com")
#定位到要懸停的元素
above = driver.find_element_by_id("xx")
#對定位到的元素執行懸停操作
ActionChains(driver).move_to_element(above).perform()
```

## 例子3:滑鼠雙擊操作

`double_click(on_element)`方法用於模擬滑鼠雙擊操作,用法同上。
### 程式碼實現:
```python
from selenium import webdriver
#引入ActionChains 類
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
#定位到要懸停的元素
double_click = driver.find_element_by_id("xx")
#對定位到的元素執行雙擊操作
ActionChains(driver).double_click(double_click).perform()
```
## 例子4:滑鼠推放操作

drag_and_drop(source, target)在源元素上按下滑鼠左鍵,然後移動到目標元素上釋放。
* source: 滑鼠拖動的源元素。
* target: 滑鼠釋放的目標元素。
程式碼實現:
```python
from selenium import webdriver
#引入ActionChains 類
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
#定位元素的源位置
element = driver.find_element_by_name("xxx")
#定位元素要移動到的目標位置
target = driver.find_element_by_name("xxx")
#執行元素的拖放操作
ActionChains(driver).drag_and_drop(element,target).perform() 
```
# 4 鍵盤事件
有時候我們在測試時需要使用`Tab` 鍵將焦點轉移到下一個元素,`Keys()`類提供鍵盤上幾乎所有按鍵的方法,前面瞭解到`send_keys()`方法可以模擬鍵盤輸入,除此之外它還可以模擬鍵盤上的一些組合鍵,例:`Ctrl+A`、`Ctrl+C` 等。
## 4.1 鍵盤操作 
`from selenium.webdriver.common.keys import Keys` #在使用鍵盤按鍵方法前需要先匯入`keys` 類包。
下面經常使用到的鍵盤操作:

* send_keys(Keys.BACK_SPACE) 刪除鍵(BackSpace) 
* send_keys(Keys.SPACE) 空格鍵(Space) 
* send_keys(Keys.TAB) 製表鍵(Tab) 
* send_keys(Keys.ESCAPE) 回退鍵(Esc) 
* send_keys(Keys.ENTER) 回車鍵(Enter) 
* send_keys(Keys.CONTROL,'a') 全選(Ctrl+A) 
* send_keys(Keys.CONTROL,'c') 複製(Ctrl+C) 
* send_keys(Keys.CONTROL,'x') 剪下(Ctrl+X) 
* send_keys(Keys.CONTROL,'v') 貼上(Ctrl+V) 
* send_keys(Keys.F1) 鍵盤F1 …… 
* send_keys(Keys.F12) 鍵盤F12
### 例子:
```python
from selenium import webdriver
#引入Keys 模組
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
#輸入框輸入內容
driver.find_element_by_id("kw").send_keys("seleniumm")
#刪除多輸入的一個m
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
#輸入空格鍵+“教程”
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys(u"教程")
#ctrl+a 全選輸入框內容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
#ctrl+x 剪下輸入框內容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
#ctrl+v 貼上內容到輸入框
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
#通過回車鍵盤來代替點選操作
driver.find_element_by_id("su").send_keys(Keys.ENTER)
driver.quit() 
```
# 5 設定元素等待
如今大多數的web應用程式使用*AJAX* 技術。當瀏覽器在載入頁面時,頁面內的元素可能並不是同時被載入完成的, 這給元素的定位新增的困難。如果因為在載入某個元素時延遲而造成`ElementNotVisibleException` 的情況出現,那麼就會降低的自動化指令碼的穩定性。
`WebDriver` 提供了兩種型別的等待:顯式等待和隱式等待。
## 5.1 顯式等待
顯式等待使`WebdDriver` 等待某個條件成立時繼續執行,否則在達到最大時長時拋棄超時異常(`TimeoutException`)。
### 例子:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
element = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,"kw")))
element.send_keys('selenium')
driver.quit()
```
#### WebDriverWait()

它是由`webdirver` 提供的等待方法。在設定時間內,預設每隔一段時間檢測一次當前頁面元素是否存
在,如果超過設定時間檢測不到則丟擲異常。具體格式如下:

`WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)`
* driver - WebDriver 的驅動程式(Ie, Firefox,Chrome 等)
* timeout - 最長超時時間,預設以秒為單位
* poll_frequency - 休眠時間的間隔(步長)時間,預設為0.5 秒
* ignored_exceptions - 超時後的異常資訊,預設情況下拋NoSuchElementException 異常。

#### until()

`WebDriverWait()`一般由`until()`(或`until_not()`)方法配合使用,下面是`until()`和`until_not()`方法的說明。

`until(method, message=’ ’)`
呼叫該方法提供的驅動程式作為一個引數,直到返回值為Ture。

`until_not(method, message=’ ’)`
呼叫該方法提供的驅動程式作為一個引數,直到返回值為False。

#### Expected Conditions

在本例中,我們在使用`expected_conditions` 類時對其時行了重新命名,通過as 關鍵字對其重新命名為`EC`,
並呼叫`presence_of_element_located()`判斷元素是否存在。
`expected_conditions` 類提供一些預期條件的實現。
* title_is 用於判斷標題是否xx。
* title_contains 用於判斷標題是否包含xx 資訊。
* presence_of_element_located 元素是否存在。
* visibility_of_element_located 元素是否可見。
* visibility_of 是否可見
* presence_of_all_elements_located 判斷一組元素的是否存在
* text_to_be_present_in_element 判斷元素是否有xx 文字資訊
* text_to_be_present_in_element_value 判斷元素值是否有xx 文字資訊
* frame_to_be_available_and_switch_to_it 表單是否可用,並切換到該表單。
* invisibility_of_element_located 判斷元素是否隱藏
* element_to_be_clickable 判斷元素是否點選,它處於可見和啟動狀態
* staleness_of 等到一個元素不再是依附於DOM。
* element_to_be_selected 被選中的元素。
* element_located_to_be_selected 一個期望的元素位於被選中。
* element_selection_state_to_be 一個期望檢查如果給定的元素被選中。
* element_located_selection_state_to_be 期望找到一個元素並檢查是否選擇狀態
* alert_is_present 預期一個警告資訊

除了`expected_conditions` 所提供的預期方法,我們也可以使用前面學過的`is_displayed()`方法來判斷元素是否可顯示。

### 例子:

```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
input_ = driver.find_element_by_id("kw")
element = WebDriverWait(driver,5,0.5).until(lambda driver : input_.is_displayed())
input_.send_keys('selenium')
driver.quit() 
```

## 5.2 隱式等待
隱式等待是通過一定的時長等待頁面所元素載入完成。哪果超出了設定的時長元素還沒有被載入測拋`NoSuchElementException` 異常。`WebDriver` 提供了`implicitly_wait()`方法來實現隱式等待,預設設定為0。它的用法相對來說要簡單的多。
### 例子:
```python
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
input_ = driver.find_element_by_id("kw22")
input_.send_keys('selenium')
driver.quit()
```

`implicitly_wait()`預設引數的單位為秒,本例中設定等待時長為10 秒,首先這10 秒並非一個固定的等待時間,它並不影響指令碼的執行速度。其次,它並不真對頁面上的某一元素進行等待,當指令碼執行到某個元素定位時,如果元素可定位那麼繼續執行,如果元素定位不到,那麼它將以輪詢的方式不斷的判斷元素
是否被定位到,假設在第6 秒鐘定位到元素則繼續執行。直接超出設定時長(10 秒)還沒定位到元素則丟擲異常。
在上面的例子中,顯然百度輸入框的定位id=kw22 是有誤的,那麼在超出10 秒後將丟擲異常。

## 5.3 sleep 休眠方法
有時間我們希望指令碼執行到某一位置時做固定時間的休眠,尤其是在指令碼除錯的過程中。那麼可以使用`sleep()`方法,需要說明的是`sleep()`由Python 的time 模組提供。
### 例子:
```python
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
sleep(2)
driver.find_element_by_id("kw").send_keys("webdriver")
driver.find_element_by_id("su").click()
sleep(3)
driver.quit()
```
當執行到`sleep()`方法時會固定的休眠所設定的時長,然後再繼續執行。`sleep()`方法預設引數以秒為單位,如果設定時長小於1 秒,可以用小數點表示,如:`sleep(0.5)`
7 多視窗切換
有時候需要在不同的視窗切換,從而操作不同的視窗上的元素,WebDriver 提供了`switch_to_window()`方法可以切換到任意的視窗。

### 例子:
```python
from selenium import webdriver
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
#****獲得百度搜索視窗控制代碼# 
sreach_windows = driver.current_window_handle
driver.find_element_by_link_text(u'****登入').click()
driver.find_element_by_link_text(u"****立即註冊").click()
#****獲得當前所有開啟的視窗的控制代碼
all_handles = driver.window_handles
#****進入註冊視窗
for handle in all_handles:
    if handle != sreach_windows:
        driver.switch_to_window(handle)
        print('now register window!')
        driver.find_element_by_name("account").send_keys('username')
        driver.find_element_by_name('password').send_keys('password')
#****進入搜尋視窗**
for handle in all_handles:
    if handle == sreach_windows:
        driver.switch_to_window(handle)
        print('now sreach window!')
        driver.find_element_by_id('TANGRAM__PSP_2__closeBtn').click()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("su").click()time.sleep(5)
driver.quit()
```
### 說明:
整個指令碼的處理過程:首先開啟百度首頁,通過`current_window_handle` 獲得當前視窗的控制代碼,並給變數`sreach_handle`。接著開啟登入彈窗,在登入視窗上點選“立即註冊”從而開啟新的註冊視窗。通過window_handles 獲得當前開啟的所視窗的控制代碼,賦值給變數`all_handles`。
第一個迴圈遍歷`all_handles`,如果`handle` 不等於`sreach_handle`,那麼一定是註冊視窗,因為指令碼執行只打開的兩個視窗。所以,通過`switch_to_window()`切換到註冊頁進行註冊操作。第二個迴圈類似,不過這一次判斷如果`handle` 等於`sreach_handle`,那麼切換到百度搜索頁,關閉之前開啟的登入彈窗,然後時行搜尋操作。
在本例中所有用到的新方法:

* current_window_handle 獲得當前視窗控制代碼
* window_handles 返回的所有視窗的控制代碼到當前會話
* switch_to_window() 用於切換到相應的視窗,與上一節的switch_to_frame() 是類似,前者用於不同視窗的切換,後者用於不同表單之間的切換。

# 8 警告框處理
在`WebDriver`中處理*JavaScript* 所生成的*alert*、*confirm* 以及*prompt* 是很簡單的。具體做法是使用`switch_to_alert()`方法定位到**alert/confirm/prompt**。然後使用**text/accept/dismiss/send_keys** 按需進行操做。
* text 返回alert/confirm/prompt 中的文字資訊。
* accept 點選確認按鈕。
* dismiss 點選取消按鈕,如果有的話。
* send_keys 輸入值,這個alert/confirm 沒有對話方塊就不能用了,不然會報錯。

### 例子:
```python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')#滑鼠懸停相“設定”連結
link = driver.find_element_by_link_text(u'設定')ActionChains(driver).move_to_element(link).perform()#開啟搜尋設定
driver.find_element_by_class_name('setpref').cick()#儲存設定
driver.find_element_by_css_selector('#gxszButton > a.prefpanelgo').click()#接收彈窗
driver.switch_to_alert().accept()
driver.quit() 
```
# 9 上傳檔案
檔案上傳操作也比較常見功能之一,上傳功能操作**webdriver**並沒有提供對應的方法,關鍵上傳檔案的思路。
對web 頁面的上功能,點選“上傳”按鈕需要開啟本地的Window 視窗,從視窗選擇本地檔案進行上傳,那麼**WebDriver** 對於Windows 的控制元件是無能為力的

對於web 頁面的上傳功能一般會有以下幾種方式。

* 普通上傳:普通的附件上傳都是將本地檔案的路徑作為一個值放input 標籤中,通過form 表單提交的時候將這個值提交給伺服器。
* 外掛上傳:一般是指基於Flash 與JavaScript 或Ajax 等技術所實現的上傳功能或外掛。

## 9.1 send_keys 實現上傳
對於通過`input`標籤實現的通過上傳,可以將其看作一個輸入框,通過`send_keys()`傳入本地檔案路徑從而模擬上傳功能。
### 例子:
```python
from selenium import webdriver
import os
driver = webdriver.Firefox()#開啟上傳功能頁面
file_path = 'file:///' + os.path.abspath('upfile.html')
driver.get(file_path)#定位上傳按鈕,新增本地檔案
driver.find_element_by_name("file").send_keys('D://upload_file.txt')
driver.quit()
```
通過這種方法上傳,就繞開了操作Windows 控制元件的步驟。如果能找上傳的`input `標籤,那麼基本都可以通過`send_keys()`方法向其輸入一個檔案地址來實現上傳。



# 10 操作cookie
有時候我們需要驗證瀏覽器中是否存在某個**cookie**,因為基於真實的**cookie** 的測試是無法通過白盒和整合測試完成的。`WebDriver` 提供了操作`Cookie` 的相關方法可以讀取、新增和刪除**cookie** 資訊。
## 10.1 操作cookie方法
webdriver 操作cookie 的方法有:
* get_cookies() 獲得所有cookie 資訊
* get_cookie(name) 返回有特定name 值有cookie 資訊
* add_cookie(cookie_dict) 新增cookie,必須有name 和value 值
* delete_cookie(name) 刪除特定(部分)的cookie 資訊
* delete_all_cookies() 刪除所有cookie 資訊

下面通過`get_cookies()`來獲取當前瀏覽器的**cookie** 資訊。

### 程式實現:
```python
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://www.youdao.com")# 獲得cookie 資訊
cookie= driver.get_cookies()#將獲得cookie 的資訊列印
print(cookie)
driver.quit()
```
### 執行結果:
```
============= RESTART ===============
[{u'domain': u'.youdao.com',
u'secure': False,
u'value': u'aGFzbG9nZ2VkPXRydWU=',
u'expiry': 1408430390.991375,
u'path': u'/',
u'name': u'_PREF_ANONYUSER__MYTH'},
{u'domain': u'.youdao.com',
u'secure': False,
u'value': u'1777851312@218.17.158.115',
u'expiry': 2322974390.991376,
u'path': u'/', u'name':
u'OUTFOX_SEARCH_USER_ID'},
{u'path': u'/',
u'domain': u'www.youdao.com',
u'name': u'JSESSIONID',
u'value': u'abcUX9zdw0minadIhtvcu',
u'secure': False}]
```
通過列印結果可以看出**cookie** 是以字典的形式進行存放的,知道了**cookie** 的存放形式,那麼我們就可以按照這種形式向瀏覽器中寫入**cookie** 資訊。
### 例子:
```python
from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("http://www.youdao.com")#向cookie 的name 和value 新增會話資訊。
driver.add_cookie({'name':'key-aaaaaaa', 'value':'value-bbbbbb'})#遍歷cookies 中的name 和value 資訊列印,當然還有上面新增的資訊
for cookie in driver.get_cookies():
    print( "%s -> %s" % (cookie['name'], cookie['value']))
driver.quit()
```
### 執行結果:
```
======================= RESTART ======================
YOUDAO_MOBILE_ACCESS_TYPE -> 1
_PREF_ANONYUSER__MYTH -> aGFzbG9nZ2VkPXRydWU=
OUTFOX_SEARCH_USER_ID -> -1046383847@218.17.158.115
JSESSIONID -> abc7qSE_SBGsVgnVLBvcu
key-aaaaaaa -> value-bbbbbb
```
從列印結果可以看到最後一條**cookie** 資訊是在指令碼執行過程中通`add_cookie()`方法新增的。通過遍歷得到的所**cookie** 資訊從而找到key 為“name”和“value”的特定**cookie** 的value。

那麼在什麼情況下會用到**cookie** 的操作呢?例如開發人員開發一個功能,當用戶登入後,會將使用者的使用者名稱寫入瀏覽器**cookie**,指定的key 為“username”,那麼我們就可以通過`get_cookies()` 找到useranme,列印vlaue,如果找不到username 或對應的value 為空,那麼說明儲存瀏覽器的cookie 是有問題的。

`delete_cookie()` 和`delete_all_cookies()` 的使用也很簡單,前者通過name 值到一個特定的cookie 將其刪除,後者直接刪除瀏覽器中的所有`cookies()`資訊。

# 11 呼叫JavaScript控制瀏覽器滾動條
`WebDiver` 不能操作本地Windows 控制元件,但對於瀏覽器上的控制元件也不是都可以操作的。比哪瀏覽器上的滾動條,雖然`WebDriver` 提供操作瀏覽器的前進和後退按鈕,但對於滾動條並沒有提供相應用的方法。那麼在這種情況下就可以藉助JavaScript 方法來控制瀏覽器滾動條。`WebDriver` 提供了`execute_script()`方法來執行**JavaScript** 程式碼。

一般用到操作滾動條的會兩個場景:
* 註冊時的法律條文的閱讀,判斷使用者是否閱讀完成的標準是:滾動條是否拉到最下方。
* 要操作的頁面元素不在視覺範圍,無法進行操作,需要拖動滾動條。


### 例子:
```html
<body onload= "document.body.scrollTop=0 ">** <body onload= "document.body.scrollTop=100000 ">
```

`document.body.scrollTop`網頁被捲去的高。

`scrollTop` 設定或獲取滾動條與最頂端之間的距離。如果想讓滾動條處於頂部,那麼可以設定`scrollTop` 的值為0,如果想讓滾動條處於最底端,可以將這個值設定的足夠大,大個視窗的高度即可。`scrollTop` 的值以畫素為單位。
### 例子:
```python
from selenium import webdriver
import time#訪問百度
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")#搜尋
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)
#將頁面滾動條拖到底部
js="document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(3)
#將滾動條移動到頁面的頂部
js_="document.documentElement.scrollTop=0"
driver.execute_script(js_)
time.sleep(3)
driver.quit()
```
通過瀏覽器開啟百度進行搜尋,搜尋的一屏無法完全顯示將會出現滾動條。這個時候就可以通過**JavaScript** 程式碼控制滾動條在任意位置,需要改變的就是`scrollTop` 的值。通過`execute_script()`方法來執行這段**JavaScript** 程式碼。

有時候滾動條不僅上下有,如上圖,其它左右也有,那麼可以通過下面**JavaScript** 程式碼來實現上下與左右滾動條的任意推動。

### 例子:
```python
# window.scrollTo(左邊距,上邊距);
# window.scrollTo(0,450);
# js=" window.scrollTo(200,1000);"
# driver.execute_script(js)
```
或者參考這篇文章控制:通過`selenium`控制瀏覽器滾動條
用法與同上,通過`execute_script()`呼叫此程式碼,修改`scrollTo()`的引數即可。
當然,**JavaScript** 的作用不僅於此,它同樣可操作頁面上的元素或讓,或讓這個元素隱藏。