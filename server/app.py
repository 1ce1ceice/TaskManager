from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from server.model import Task 

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'POST':
        data = request.get_json()
        task = Task(title=data['title'], description=data['description'])
        db.session.add(task)
        db.session.commit()
        return jsonify({'id': task.id}), 201
    else:
        all_t = Task.query.all()
        return jsonify([
            {'id': t.id, 'title': t.title, 'description': t.description, 'completed': t.completed}
            for t in all_t
        ])

if __name__ == '__main__':
    app.run(debug=True)
