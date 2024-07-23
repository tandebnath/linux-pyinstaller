from flask import Flask, request, jsonify, render_template
import webview
import threading
from api import Api

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save-directory', methods=['POST'])
def save_directory():
    data = request.get_json()
    directory_path = data['path']
    print(f"Received directory path: {directory_path}")
    return jsonify({'status': 'success'})

def start_server():
    app.run()

if __name__ == '__main__':
    # Start Flask server in a separate thread
    threading.Thread(target=start_server).start()
    
    # Start PyWebview to create a GUI
    api_instance = Api()
    window = webview.create_window('Directory Selector', 'http://127.0.0.1:5000', js_api=api_instance)
    webview.start()
