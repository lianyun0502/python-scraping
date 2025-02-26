## HTTP協議對資源的操作

|     方法     |             說明              |
|:----------:|:---------------------------:|
|   *GET	    |        請求獲取URL位置的資源         |
|   HEAD	    |請求獲取URL位置資源的響應消息報告，即獲得資源的頭部信息|
|   *POST	   |     請求向URL位置的資源後附加新的消息      |
|   *PUT	    | 請求向URL位置存儲一個資源，覆蓋原URL位置的資源  |
|   PATCH	   | 請求局部更新URL位置的資源,即改變該處資源的部分內容 |
| *DELETE	   |       請求刪除URL位置存儲的資源        |

以上方法中，GET,HEAD是從伺服器獲取信息到本地，PUT,POST,PATCH,DELETE是從本地向伺服器提交信息。通過URL和命令管理資源，操作獨立無狀態，網絡通道及伺服器成了黑盒子。

## HTTP協議對資源的描述

|     方法     |             說明              |
|:----------:|:---------------------------:|
|   OPTIONS	|   請求查看支持的HTTP請求方法，伺服器會返回該資源所支持的所有HTTP請求方法 |
|   TRACE	   |   請求查看經過的代理伺服器收到的請求信息，主要用於測試或診斷 |
|   CONNECT	|   請求用隧道協議連接代理，實現用隧道協議代理安全的SSL/TLS連接 |