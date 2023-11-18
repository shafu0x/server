from flask import Flask, jsonify, request

app = Flask(__name__)

# Route to get all tasks
@app.route('/games', methods=['GET'])
def get_tasks():
    return jsonify({'game': "0"})

@app.route('/tokens/<address>', methods=['GET'])
def get_tokens():
    return jsonify({'hasToken': "99"})
