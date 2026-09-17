from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory storage for our To-Do items
todos = []
current_id = 1

@app.route('/api/todos', methods=['GET'])
def get_todos():
    """Retrieve all current to-do tasks."""
    return jsonify(todos)

@app.route('/api/todos', methods=['POST'])
def add_todo():
    """Add a new task to our to-do list."""
    global current_id
    data = request.get_json()
    
    if not data or not data.get('task'):
        return jsonify({'error': 'Task content is required'}), 400
        
    todo = {
        'id': current_id, 
        'task': data.get('task'), 
        'completed': False
    }
    todos.append(todo)
    current_id += 1
    
    return jsonify(todo), 201

@app.route('/api/todos/<int:todo_id>', methods=['PUT', 'PATCH'])
def update_todo(todo_id):
    """Update a task's title or status."""
    global todos
    data = request.get_json()
    for todo in todos:
        if todo['id'] == todo_id:
            if 'task' in data:
                todo['task'] = data['task']
            if 'completed' in data:
                todo['completed'] = data['completed']
            return jsonify(todo)
    return jsonify({'error': 'Task not found'}), 404

@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Delete a task by ID."""
    global todos
    todos = [t for t in todos if t['id'] != todo_id]
    return '', 204

if __name__ == '__main__':
    # Running API server on port 5000
    app.run(port=5000, debug=True)
