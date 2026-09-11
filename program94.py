import tkinter as tk
from tkinter import messagebox

def handle_key(event):
    if event.char:
        char_label.config(text=f"Last character typed: {event.char}")

def handle_click(event):
    status_label.config(text="Status: Clicked inside the routine area!")

def check_routine():
    task = task_entry.get().strip()
    if not task:
        messagebox.showwarning("Warning", "No task entered! Please input your current task.")
        return
        
    next_task = "Check homework and study"
    routine_display.delete("1.0", tk.END)
    routine_display.insert(tk.END, f"Current Task: {task}\n\nNext Routine Step: {next_task}")

root = tk.Tk()
root.title("After-School Routine Checker")
root.geometry("450x400")

entry_label = tk.Label(root, text="Type your current after-school task:")
entry_label.pack(pady=5)

task_entry = tk.Entry(root, width=35)
task_entry.pack(pady=5)
task_entry.bind("<KeyRelease>", handle_key)

char_label = tk.Label(root, text="Last character typed: None")
char_label.pack(pady=2)

routine_frame = tk.Frame(root, width=300, height=60, bg="#e0e0e0", bd=1, relief="solid")
routine_frame.pack(pady=15)
routine_frame.pack_propagate(False)

routine_label = tk.Label(routine_frame, text="Click inside this routine area", bg="#e0e0e0")
routine_label.pack(expand=True)
routine_frame.bind("<Button-1>", handle_click)
routine_label.bind("<Button-1>", handle_click)

status_label = tk.Label(root, text="Status: Ready")
status_label.pack(pady=2)

check_button = tk.Button(root, text="Check Routine", command=check_routine)
check_button.pack(pady=10)

routine_display = tk.Text(root, width=45, height=6)
routine_display.pack(pady=10)

root.mainloop()
