from flask import Flask, jsonify, request
from notifier import main

import os
from dotenv import load_dotenv

app = Flask(__name__)

def authenticate_api_key(api_key):
    
    load_dotenv()
    flask_key = {api_key: os.getenv("flask_key")}
    
    return flask_key.get(api_key)

@app.before_request
def before_request():
    api_key = request.headers.get('key')
    if not api_key or not authenticate_api_key(api_key):
        return jsonify({'error': 'Unauthorized'}), 401

@app.route('/traffic', methods=['POST'])
def get_traffic():
    headers = dict(request.headers)
    content_type = headers['Content-Type']
    if content_type == 'application/json':
        data = request.get_json()
        road = data['road']
        start = data['segment_start']
        end = data['segment_end']
        resp_dict = [main(road_of_interest=road, segment_start=start, segment_end=end)]

        return jsonify({'response': resp_dict})
    else:
        return jsonify({'Error': 'Unsupported content-type. Please supply json content'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7000)