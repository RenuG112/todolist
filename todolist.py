import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")

# Input frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Listbox frame
listbox_frame = tk.Frame(root)
listbox_frame.pack(pady=10)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Input field and add button
task_entry = tk.Entry(input_frame, width=20, font=('Arial', 14))
task_entry.grid(row=0, column=0, padx=10)

def add_task():
    task = task_entry.get()
    if task:
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

add_button = tk.Button(input_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=1)

# Listbox to display tasks
listbox = tk.Listbox(listbox_frame, width=40, height=10, font=('Arial', 14), selectmode=tk.SINGLE)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(listbox_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Functions for removing and clearing tasks
def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to remove.")

def clear_tasks():
    listbox.delete(0, tk.END)

# Buttons for removing and clearing tasks
remove_button = tk.Button(button_frame, text="Remove Task", command=remove_task)
remove_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear Tasks", command=clear_tasks)
clear_button.grid(row=0, column=1, padx=10)

root.mainloop()
