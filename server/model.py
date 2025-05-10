from server.app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500))
    completed = db.Column(db.Boolean, default=False)

    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def __repr__(self):
        return f"<Task {self.title}>"
