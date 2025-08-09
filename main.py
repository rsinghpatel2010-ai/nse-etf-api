from flask import Flask, request, jsonify
import pandas as pd
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Render + Flask!"

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "name": "Raghvendra",
        "business": "Bajrang Printers"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
