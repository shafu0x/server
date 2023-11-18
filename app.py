from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
tasks = [
    {
        'id': 1,
        'title': 'Task 1',
        'done': False
    },
    {
        'id': 2,
        'title': 'Task 2',
        'done': False
    }
]

# Route to get all tasks
@app.route('/games', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})
