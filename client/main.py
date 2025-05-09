import tkinter as tk
from controller import TaskController

def main():
    root = tk.Tk()
    controller = TaskController(root)
    controller.refresh()
    root.mainloop()

if __name__ == '__main__':
    main()
