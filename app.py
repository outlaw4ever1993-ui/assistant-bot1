from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return {
        'status': 'ok',
        'message': 'Assistant Bot is running',
        'version': '1.0.0'
    }, 200

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=False)

