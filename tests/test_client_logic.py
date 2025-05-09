from client.model import add_task, get_tasks, update_task, delete_task

def test_task_crud(monkeypatch):
    class DummyResp:
        def __init__(self, json_data, status_code=200):
            self._json = json_data
            self.status_code = status_code
        def json(self):
            return self._json
        def raise_for_status(self):
            pass

    tasks = [{'id': 1, 'title': 'T', 'description': '', 'completed': False}]
    monkeypatch.setattr('client.model.requests.get', lambda url: DummyResp(tasks))
    got = get_tasks()
    assert got[0].title == 'T'
