# 自毀消息網頁

這是一個簡單的自毀消息網頁應用，用戶閱讀消息後點擊按鈕，消息將被銷毀，再次訪問時將不再顯示。

## 本地安裝與運行

1. 確保已安裝 Python 3.6 或更高版本
2. 安裝依賴：

```bash
pip install -r requirements.txt
```

3. 運行：

```bash
python app.py
```

服務器啟動後，在瀏覽器中訪問 http://127.0.0.1:5000/ 即可查看消息。

## 功能

- 首次訪問時顯示消息和"已閱讀完畢"按鈕
- 點擊按鈕後，消息將被銷毀
- 再次訪問同一URL時，將顯示消息已被銷毀的提示
- 使用JSON文件存儲消息狀態
- 重置功能受密碼保護
- 從外部文件加載消息內容，方便修改
- 現代化視覺效果，包括動畫和互動元素

## 新增視覺效果

應用包含以下現代化視覺效果：

### 消息頁面
- 粒子背景效果，與鼠標互動
- 消息打字機效果與淡入動畫
- 按鈕點擊漣漪動畫
- 30秒自動閱讀倒計時
- 深色模式設計，提高閱讀舒適度

### 消息銷毀頁面
- 文件燃燒動畫效果
- 漂浮灰燼特效
- 火焰背景動畫

### 重置頁面
- 動態星空背景
- 鎖頭解鎖動畫
- 密碼框顯示/隱藏切換功能
- 錯誤提示動畫效果

## 修改消息內容

您可以直接編輯 `message_content.txt` 文件來自定義顯示的消息內容：
1. 打開 `message_content.txt` 文件
2. 修改文件中的文字內容（支持多行文本）
3. 保存文件
4. 無需重啟服務器，系統會自動讀取最新的內容

## 重置消息

如果需要重置消息狀態，請訪問 /reset 路徑，並輸入重置密碼。
默認密碼是 `reset123`。

## 部署到公開網域

### 使用JSON文件存儲的注意事項

此應用使用JSON文件 (`message_status.json`) 來存儲消息狀態，並使用文本文件 (`message_content.txt`) 存儲消息內容。在部署到雲平台時，需要注意以下幾點：

1. **臨時文件系統**：許多雲平台（如Heroku）使用臨時文件系統，這意味著：
   - 在應用重啟或平台維護時，JSON文件和消息內容可能會被刪除
   - 每次部署新版本時，文件也會被重置
   - 結果：消息狀態可能會意外重置為未讀，消息內容恢復為默認

2. **適用場景**：
   - 此應用最適合部署在具有持久化文件系統的平台（如VPS、PythonAnywhere等）
   - 如果僅用於臨時展示，任何平台都可以
   - 對於需要長期保存的重要消息，建議考慮使用數據庫版本

### 部署到 Heroku

1. 註冊 [Heroku](https://www.heroku.com/) 帳號

2. 安裝 [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

3. 登入 Heroku:
```bash
heroku login
```

4. 創建 Heroku 應用:
```bash
heroku create your-app-name
```

5. 設置環境變數:
```bash
heroku config:set SECRET_KEY=your-secret-key
heroku config:set RESET_PASSWORD=your-reset-password
```

6. 部署到 Heroku:
```bash
git push heroku main
```

### 部署到 PythonAnywhere（推薦，有持久化文件系統）

1. 註冊 [PythonAnywhere](https://www.pythonanywhere.com/) 帳號

2. 創建 Web 應用並選擇 Flask 框架

3. 上傳項目文件或使用 Git 克隆

4. 設置 WSGI 文件指向 app.py 中的 app 變數

5. 設置環境變數 SECRET_KEY 和 RESET_PASSWORD

6. 重新加載 Web 應用

### 其他雲平台選項（有持久化文件系統）

- Railway.app
- Render.com
- DigitalOcean App Platform
- 傳統虛擬機或容器服務 (AWS, GCP, Azure 等)
  - 安裝 Python 和項目依賴
  - 使用 gunicorn 運行應用: `gunicorn app:app`
  - 配置 Nginx 或其他前端服務器

## 安全性考慮

- 在生產環境中，請更改默認的重置密碼
- 使用環境變數設置 SECRET_KEY 和 RESET_PASSWORD
- 如果需要更高的安全性，可以考慮切換到數據庫版本 

## 外部資源

應用使用了以下外部資源：

- particles.js - https://vincentgarreau.com/particles.js/ - 用於粒子效果
- GIPHY - 用於火焰背景動畫
- PNG Item - 用於紙張圖片資源 