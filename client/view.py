import tkinter as tk
from tkinter import messagebox

class TaskView:
    def __init__(self, root):
        self.root = root
        root.title('Task Manager')

        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.listbox = tk.Listbox(self.frame, width=50)
        self.listbox.grid(row=0, column=0, columnspan=2)

        tk.Button(self.frame, text='Refresh').grid(row=1, column=0)
        tk.Button(self.frame, text='Add').grid(row=1, column=1)
