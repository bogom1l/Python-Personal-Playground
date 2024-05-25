import tkinter as tk
from tkinter import messagebox
import os
import json

TODO_FILE = "todos.json"


def load_todos():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as file:
        return json.load(file)


def save_todos(todos):
    with open(TODO_FILE, 'w') as file:
        json.dump(todos, file)


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List v1")

        self.todos = load_todos()

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.listbox = tk.Listbox(self.frame, width=55, height=12)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_todo)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_todo)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_todo)
        self.delete_button.pack(pady=5)

        self.delete_all_button = tk.Button(root, text="Delete All Tasks", command=self.delete_all_todos)
        self.delete_all_button.pack(pady=5)

        self.mark_all_completed_button = tk.Button(root, text="Mark All Completed", command=self.mark_all_completed)
        self.mark_all_completed_button.pack(pady=5)

        self.unmark_all_button = tk.Button(root, text="Mark All Uncompleted", command=self.unmark_all)
        self.unmark_all_button.pack(pady=5)

        self.search_entry = tk.Entry(root, width=25)
        self.search_entry.pack(pady=10)

        self.search_button = tk.Button(root, text="Search Task", command=self.search_todo)
        self.search_button.pack(pady=5)

        self.refresh_list()

    def refresh_list(self, todos=None):
        self.listbox.delete(0, tk.END)
        todos = todos or self.todos
        for idx, todo in enumerate(todos, 1):
            status = "✓" if todo["completed"] else "X"
            self.listbox.insert(tk.END, f"{idx}. [{status}] {todo['task']}")

    def add_todo(self):
        task = self.entry.get()
        if task:
            self.todos.append({"task": task, "completed": False})
            save_todos(self.todos)
            self.entry.delete(0, tk.END)
            self.refresh_list()
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty")

    def complete_todo(self):
        try:
            selected = self.listbox.curselection()[0]
            self.todos[selected]["completed"] = True
            save_todos(self.todos)
            self.refresh_list()
        except IndexError:
            messagebox.showwarning("Selection Error", "No task selected")

    def delete_todo(self):
        try:
            selected = self.listbox.curselection()[0]
            self.todos.pop(selected)
            save_todos(self.todos)
            self.refresh_list()
        except IndexError:
            messagebox.showwarning("Selection Error", "No task selected")

    def delete_all_todos(self):
        if messagebox.askyesno("Delete All", "Are you sure you want to delete all tasks?"):
            self.todos = []
            save_todos(self.todos)
            self.refresh_list()

    def mark_all_completed(self):
        for todo in self.todos:
            todo["completed"] = True
        save_todos(self.todos)
        self.refresh_list()

    def unmark_all(self):
        for todo in self.todos:
            todo["completed"] = False
        save_todos(self.todos)
        self.refresh_list()

    def search_todo(self):
        keyword = self.search_entry.get().lower()
        if keyword:
            filtered_todos = [todo for todo in self.todos if keyword in todo["task"].lower()]
            self.refresh_list(filtered_todos)
        else:
            messagebox.showwarning("Input Error", "Search keyword cannot be empty")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()