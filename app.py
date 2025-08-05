import os
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return 'File server is running!'

@app.route('/files/<path:filename>')
def serve_file(filename):
    return send_from_directory('static', filename)
    
@app.route('/.well-known/<path:filename>')
def well_known_files(filename):
    return send_from_directory('.well-known', filename)
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
