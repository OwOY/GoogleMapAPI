<div align=center>
  <img src="https://cdn.iconscout.com/icon/free/png-256/google-maps-2863735-2378123.png">
</div>

----  
### API_KEY
1. 需建立Google帳戶
2. 進入Google Cloud Platform(GCP)
3. 建立專案
4. 選擇API和服務 > 程式庫 選擇想要之API
5. 進入憑證頁面選擇上方建立憑證
6. 完成！
----  
### 
- Geocode  
>> 解析輸入位置之座標
```
API = https://maps.googleapis.com/maps/api/geocode/json?{params}
```  
文件參考  
https://developers.google.com/maps/documentation/geocoding/overview?hl=zh_TW
----  
- StaticMap  
>> 匯出靜態google map，並根據參數輸出圖案  
```
API = https://maps.googleapis.com/maps/api/staticmap?{params}
```
文件參考  
https://developers.google.com/maps/documentation/maps-static/start?hl=zh_TW
