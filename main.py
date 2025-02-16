import tkinter as tk
from tkinter import messagebox
import json

TODO_FILE = "tasks.json"

def load_tasks():
    """Load tasks from file if available."""
    try:
        with open(TODO_FILE, "r") as file:
            tasks = json.load(file)
            for task in tasks:
                listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass

def save_tasks():
    """Save tasks to a file."""
    tasks = list(listbox.get(0, tk.END))
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file)

def add_task():
    """Add a task to the list."""
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Enter a task!")

def remove_task():
    """Remove the selected task."""
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to remove!")

def clear_all():
    """Clear all tasks."""
    listbox.delete(0, tk.END)
    save_tasks()

# GUI setup
root = tk.Tk()
root.title("To-Do List App")
root.geometry("500x550")  # Increased window size
root.configure(bg="#ADD8E6")  # Light blue background

# Centering the frame
frame = tk.Frame(root, bg="#ADD8E6")
frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)  # Centering the listbox

# Enlarged listbox
listbox = tk.Listbox(frame, width=50, height=12, font=("Arial", 14), bg="white", fg="black")
listbox.pack(side=tk.LEFT, padx=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(root, width=45, font=("Arial", 14))
entry.place(relx=0.5, rely=0.65, anchor=tk.CENTER)  # Centering entry box

# Buttons placed below entry
btn_add = tk.Button(root, text="Add Task", command=add_task, bg="#4CAF50", fg="white", font=("Arial", 12), padx=20, pady=5)
btn_add.place(relx=0.3, rely=0.75, anchor=tk.CENTER)

btn_remove = tk.Button(root, text="Remove Task", command=remove_task, bg="#FF5733", fg="white", font=("Arial", 12), padx=20, pady=5)
btn_remove.place(relx=0.7, rely=0.75, anchor=tk.CENTER)

btn_clear = tk.Button(root, text="Clear All", command=clear_all, bg="#2196F3", fg="white", font=("Arial", 12), padx=20, pady=5)
btn_clear.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

# Load tasks on startup
load_tasks()

root.mainloop()
