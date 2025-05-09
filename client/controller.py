from model import get_tasks, add_task, update_task, delete_task
from view import TaskView
import tkinter as tk
from tkinter import simpledialog

class TaskController:
    def __init__(self, root):
        self.view = TaskView(root)
        self._bind_events()

    def _bind_events(self):
        self.view.frame.grid_slaves(row=1, column=0)[0].config(command=self.refresh)
        self.view.frame.grid_slaves(row=1, column=1)[0].config(command=self.create_task)

    def refresh(self):
        self.view.listbox.delete(0, tk.END)
        tasks = get_tasks()
        for t in tasks:
            self.view.listbox.insert(tk.END, f"{t.id}: {t.title} - {'Done' if t.completed else 'Pending'}")

    def create_task(self):
        title = simpledialog.askstring("Title", "Task title:")
        if title:
            description = simpledialog.askstring("Description", "Task description:")
            add_task(title, description or '')
            self.refresh()
