import pytest
from unittest import mock
from client.model import get_tasks, add_task, update_task, delete_task

API_URL = 'http://127.0.0.1:5000/tasks'

def test_get_tasks():
    mock_response = [
        {"id": 1, "title": "Test Task 1", "description": "Test Description 1", "completed": False},
        {"id": 2, "title": "Test Task 2", "description": "Test Description 2", "completed": True}
    ]
    
    with mock.patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        
        tasks = get_tasks()
        
        assert len(tasks) == 2
        assert tasks[0].title == "Test Task 1"
        assert tasks[1].completed is True

def test_add_task():
    mock_response = {"id": 3}
    
    with mock.patch('requests.post') as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = mock_response
        
        task_id = add_task("New Task", "New Description")
        
        assert task_id == 3

def test_update_task():
    with mock.patch('requests.put') as mock_put:
        mock_put.return_value.status_code = 200
        
        update_task(1, title="Updated Task", completed=True)
        
        mock_put.assert_called_once_with(f"{API_URL}/1", json={"title": "Updated Task", "completed": True})

def test_delete_task():
    with mock.patch('requests.delete') as mock_delete:
        mock_delete.return_value.status_code = 200
        
        delete_task(1)
        
        mock_delete.assert_called_once_with(f"{API_URL}/1")
