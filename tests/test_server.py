import pytest
from server import app, db, Task

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    with app.app_context():
        db.create_all()
        yield client
        db.drop_all()

def test_add_and_get_task(client):
    res = client.post('/tasks', json={'title': 'Test', 'description': 'Desc'})
    assert res.status_code == 201
    data = client.get('/tasks').get_json()
    assert len(data) == 1
    assert data[0]['title'] == 'Test'