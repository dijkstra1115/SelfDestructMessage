# 自毀消息網站資源說明

需要下載以下文件以完善網站功能：

## 圖標和圖片資源

1. **網站圖標**
   - 文件名: favicon.ico
   - 位置: static/favicon.ico
   - 推薦來源: https://favicon.io/

2. **火焰背景**
   - 文件名: fire.gif
   - 位置: static/images/fire.gif
   - 建議: 火焰動態GIF，透明或深色背景

3. **燃燒紙張**
   - 文件名: burning-paper.gif
   - 位置: static/images/burning-paper.gif
   - 建議: 紙張被燃燒的動畫

## JavaScript 資源

如果使用本地文件出現問題，可以在message.html中直接使用CDN引入particles.js:
```html
<script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
```

## 本地測試說明

1. 安裝Python依賴
```
pip install -r requirements.txt
```

2. 啟動應用
```
python app.py
```

3. 訪問網址
```
http://127.0.0.1:5000/
```

## 重置說明

重置密碼: reset123

訪問 http://127.0.0.1:5000/reset 並輸入密碼可重置消息狀態。 
