from flask import Flask, jsonify
from main import main

road_of_interest = "A1"

app = Flask(__name__)
resp_dict = [main(road_of_interest)]

@app.route('/traffic', methods=['GET'])
def get_traff():
    return jsonify({'response': resp_dict})

if __name__ == '__main__':
    app.run(debug=True)