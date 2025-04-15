from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import json
import hashlib

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24))  # 從環境變數獲取密鑰或生成隨機密鑰

# 消息狀態文件路徑
STATUS_FILE = 'message_status.json'

# 重置密碼的哈希值 (默認密碼為 'reset123')
# 在生產環境中應該使用環境變數設置
DEFAULT_RESET_PASSWORD = 'reset123'
RESET_PASSWORD_HASH = hashlib.sha256(os.environ.get('RESET_PASSWORD', DEFAULT_RESET_PASSWORD).encode()).hexdigest()

def load_status():
    """加載消息狀態"""
    if os.path.exists(STATUS_FILE):
        try:
            with open(STATUS_FILE, 'r') as f:
                return json.load(f)
        except Exception:
            return {'read': False, 'last_updated': None}
    return {'read': False, 'last_updated': None}

def save_status(status):
    """保存消息狀態"""
    with open(STATUS_FILE, 'w') as f:
        json.dump(status, f)

@app.route('/', methods=['GET', 'POST'])
def index():
    status = load_status()
    
    if request.method == 'POST':
        # 當用戶點擊"已閱讀完畢"按鈕時
        status['read'] = True
        import datetime
        status['last_updated'] = datetime.datetime.now().isoformat()
        save_status(status)
        return redirect(url_for('index'))
    
    # 檢查消息是否已經被閱讀過
    if status['read']:
        return render_template('empty.html')
    else:
        return render_template('message.html', message="這是一條自毁消息。閱讀後將不再顯示。")

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    """重置消息狀態（受密碼保護）"""
    if request.method == 'POST':
        password = request.form.get('password', '')
        # 計算輸入密碼的哈希值並與存儲的哈希值比較
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        if password_hash == RESET_PASSWORD_HASH:
            import datetime
            status = {'read': False, 'last_updated': datetime.datetime.now().isoformat()}
            save_status(status)
            return redirect(url_for('index'))
        else:
            return render_template('reset.html', error="密碼錯誤")
    
    return render_template('reset.html')

if __name__ == '__main__':
    # 在本地開發使用
    app.run(debug=True)
else:
    # 生產環境使用
    # gunicorn或其他WSGI服務器會直接使用app變數
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', os.urandom(24))