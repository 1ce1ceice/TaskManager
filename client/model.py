import requests

API_URL = 'http://127.0.0.1:5000/tasks'

class Task:
    def __init__(self, id, title, description, completed):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

def get_tasks():
    response = requests.get(API_URL)
    response.raise_for_status()
    return [Task(**data) for data in response.json()]

def add_task(title, description):
    response = requests.post(API_URL, json={'title': title, 'description': description})
    response.raise_for_status()
    return response.json()['id']

def update_task(task_id, **kwargs):
    response = requests.put(f"{API_URL}/{task_id}", json=kwargs)
    response.raise_for_status()

def delete_task(task_id):
    response = requests.delete(f"{API_URL}/{task_id}")
    response.raise_for_status()
