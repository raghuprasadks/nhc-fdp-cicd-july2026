import os

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Sample data to return
    data = {
        'message': 'Hello, World!',
        'status': 'success'
    }
    return jsonify(data)

@app.route('/welcome', methods=['GET'])
def welcome():
    return jsonify({'message': 'Welcome to the Flask API!'})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))