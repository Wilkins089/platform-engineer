from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.get('/')
def hello() -> str:
    return 'Hello Python App'


@app.get('/status')
def status():
    return jsonify({
        "status": "ok",
        "service": "hello-python-app"
    }), 200


if __name__ == '__main__':
    port = int(os.getenv('PORT', '3000'))
    app.run(host='0.0.0.0', port=port)